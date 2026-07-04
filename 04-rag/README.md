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

**RAG** stands for **Retrieval-Augmented Generation**. Break it down:
- **Generation** = the LLM writing an answer (Module 3).
- **Retrieval** = fetching relevant information first (using embeddings, Module 2).
- **Augmented** = we *augment* the model's prompt with that fetched information.

So the recipe is: **when the user asks something, first go find the most relevant real
documents, paste them into the prompt, and instruct the model to answer using only those.**
The model stops relying on its fuzzy memory and starts answering from facts *we* supplied and
control.

> Analogy: the difference between a student answering from vague memory (and bluffing when
> unsure) versus an **open-book exam** where they must quote the textbook. RAG turns every
> answer into an open-book answer.

### Why not just put the whole manual in the prompt?
Two reasons. First, models have a limited **context window** (only so many tokens fit).
Second, dumping irrelevant text actually *hurts* answers — the model gets distracted. So we
retrieve **only the most relevant passages**. That's why we chunk and search instead of
pasting everything.

---

## The two building blocks

### 1. Chunking
We split each manual into **chunks** — here, one chunk per section (each `##` heading). Small,
focused chunks mean that when we retrieve, we get *just* the relevant procedure, not a whole
document. Chunking well is a real part of building good RAG.

### 2. A vector store
We embed every chunk (Module 2's `embed`) and keep the vectors in a **vector database**. We
use **Chroma**, a simple local one. A vector store is just a specialised container that's very
fast at answering \"which stored vectors are closest to *this* query vector?\" — which is
exactly the retrieval step.

We hand Chroma our own embeddings (computed with Ollama), so nothing needs to download and
everything stays offline.

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
