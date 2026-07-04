# Module 4 · ARIA reads the manuals (RAG) 📚

> **Story so far:** In Module 3, ARIA confidently invented a scrubber part number that doesn't
> exist. On a real colony, acting on a made-up fact could be deadly. In this module we fix
> that by giving ARIA a library card: it will look up the colony's **actual operations
> manuals** before answering, and cite them. This technique is called **RAG**, and it's
> probably the single most useful pattern in applied AI today.

**Time:** ~40 min · **Beats:** 2 Core + 1 Stretch

| Beat | What you do | Type | Time |
|---|---|---|---|
| 4a | Chunk & embed the manuals into a vector store | Core · Live-code | 20 min |
| 4b | Retrieve + ground ARIA's answers | Core · Live-code | 20 min |
| — | Evaluate the RAG system | 🌱 Stretch · Self-paced | — |

---

## What is RAG, in plain words?

**RAG** stands for **Retrieval-Augmented Generation**. It sounds intimidating, so break it
down one word at a time:
- **Generation** = the LLM writing an answer (Module 3) — the part you already know.
- **Retrieval** = fetching relevant information first (using embeddings, Module 2) — the part
  you also already know, from a different angle.
- **Augmented** = we *augment*, meaning "add to," the model's prompt with that fetched
  information before asking it to answer.

So the recipe is: **when the user asks something, first go find the most relevant real
documents, paste them into the prompt, and instruct the model to answer using only those.**
The model stops relying on its fuzzy, general memory of "things text like this usually says"
and starts answering from facts *we* supplied and control. Notice that RAG isn't really one
new idea — it's Modules 2 and 3, combined in a specific order, to fix a specific problem.

> Analogy: the difference between a student answering from vague memory (and bluffing when
> unsure) versus an **open-book exam** where they must quote the textbook. RAG turns every
> answer into an open-book answer, and "I couldn't find that in the book" becomes an
> acceptable, honest response instead of a guess.

### Why not just put the whole manual in the prompt?
Two reasons. First, models have a limited **context window** (only so many tokens fit — see
Module 3's glossary). Second, dumping irrelevant text actually *hurts* answers — the model can
get distracted by unrelated passages and produce a worse response than if it had seen only the
relevant part. So we retrieve **only the most relevant passages** for each specific question.
That's why we chunk and search instead of pasting everything in every time.

---

## The two building blocks

### 1. Chunking
We split each manual into **chunks** — here, one chunk per section (each `##` heading in the
markdown file). Small, focused chunks mean that when we retrieve, we get *just* the relevant
procedure, not a whole document mixed with unrelated sections. Chunking well (not too big, not
so small that context gets lost) is a real, practical part of building good RAG systems in the
real world.

### 2. A vector store
We embed every chunk (using the exact same `embed(...)` function from Module 2) and keep the
resulting vectors in a **vector database** — a specialised kind of storage built specifically
for one job: answering "which stored vectors are closest to *this* query vector?" as fast as
possible, even across thousands or millions of chunks. We use **Chroma**, a simple, local,
file-free vector database that's perfect for learning and small projects. That "find the
closest vectors" operation is exactly the retrieval step in RAG's name.

We hand Chroma our own embeddings (computed with Ollama), so Chroma itself never needs to
download its own model — nothing needs internet access at retrieval time, and everything
stays offline once setup is done.

---

## A helper you'll reuse later

We've packaged this whole pattern into [`../shared/rag.py`](../shared/rag.py) as a small
`RagIndex` class. In this module you'll build the pieces by hand so you understand them; in
Modules 5 and 7, ARIA will call `RagIndex` to look things up during an emergency.

---

## Prerequisites
- Ollama running with `nomic-embed-text` (for embedding) and `llama3.2` (for answering).
- The manuals in [`../data/manuals/`](../data/manuals/) — five original Orbital documents.

## Beats

### 4a · Chunk & embed → [`04a_embed_docs.ipynb`](04a_embed_docs.ipynb)
Load the five manuals, split them into sections, embed each section, and load them into a
Chroma collection you can search.

### 4b · Retrieve & ground → [`04b_retrieve_ground.ipynb`](04b_retrieve_ground.ipynb)
Ask *"What do I do if O₂ drops in Module B?"* — retrieve the right passages and have ARIA
answer **from the manual, with a citation**. Then re-ask the part-number question from Module
3 and watch a grounded ARIA correctly say it doesn't know. Hallucination, solved.

### 🌱 Stretch · Evaluate → [`stretch_evaluation.ipynb`](stretch_evaluation.ipynb)
"It looked right" is not a metric. Measure whether retrieval actually pulls the correct manual
for a set of known questions — your first taste of **AI evaluation**.

## ✅ You're done when
ARIA answers the O₂ question by citing the right manual, and declines to invent the part
number. Solution in [`solution/`](solution/).
