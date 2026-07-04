"""
rag.py — tiny retrieval-augmented-generation helper for the Orbital manuals.

Used by Module 4 (built up by hand there), and reused by Modules 5 & 7 so the agent can
look things up. Everything is local: embeddings come from Ollama, the vector store is an
in-memory Chroma collection (no download, no cloud).

    from shared.rag import RagIndex
    index = RagIndex.from_manuals()
    hits = index.retrieve("oxygen dropping in module B", k=3)
    answer = index.answer("What do I do if O2 drops?")
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from shared import orbital
from shared.llm import chat, embed


def chunk_markdown(text: str, source: str) -> list[dict]:
    """Split a markdown doc into chunks, one per section (## heading)."""
    parts = re.split(r"\n(?=#{1,3}\s)", text)
    chunks = []
    for part in parts:
        clean = part.strip()
        if len(clean) < 40:  # skip tiny fragments / title-only sections
            continue
        chunks.append({"text": clean, "source": source})
    return chunks


@dataclass
class RagIndex:
    collection: object
    chunks: list[dict]

    @classmethod
    def from_manuals(cls, manuals_dir: Path | None = None) -> "RagIndex":
        import chromadb

        manuals_dir = manuals_dir or orbital.MANUALS_DIR
        chunks: list[dict] = []
        for md in sorted(Path(manuals_dir).glob("*.md")):
            chunks.extend(chunk_markdown(md.read_text(), md.name))

        vectors = embed([c["text"] for c in chunks])

        client = chromadb.EphemeralClient()
        collection = client.create_collection("orbital_manuals")
        collection.add(
            ids=[f"chunk-{i}" for i in range(len(chunks))],
            embeddings=vectors,
            documents=[c["text"] for c in chunks],
            metadatas=[{"source": c["source"]} for c in chunks],
        )
        return cls(collection=collection, chunks=chunks)

    def retrieve(self, query: str, k: int = 3) -> list[dict]:
        qv = embed(query)[0]
        res = self.collection.query(query_embeddings=[qv], n_results=k)
        docs = res["documents"][0]
        metas = res["metadatas"][0]
        return [{"text": d, "source": m["source"]} for d, m in zip(docs, metas)]

    def answer(self, query: str, k: int = 3) -> str:
        hits = self.retrieve(query, k=k)
        context = "\n\n---\n\n".join(f"[{h['source']}]\n{h['text']}" for h in hits)
        system = (
            "You are ARIA, the Orbital colony assistant. Answer ONLY using the provided "
            "manual excerpts. If the answer is not in them, say you don't have that "
            "information. Cite the source file in square brackets."
        )
        prompt = f"Manual excerpts:\n{context}\n\nQuestion: {query}"
        return chat(prompt, system=system, temperature=0.2)
