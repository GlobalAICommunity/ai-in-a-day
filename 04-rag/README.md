# Module 4 · ARIA reads the manuals (RAG) 📚

> **Story:** In Module 3, ARIA confidently invented a part number. That's dangerous. Now
> we **ground** ARIA in Orbital's real operations manuals so its answers are based on
> facts — with citations.

**Time:** ~40 min · **Beats:** 2 Core + 1 Stretch

| Beat | What you do | Type | Time |
|---|---|---|---|
| 4a | Chunk & embed the manuals into a vector store | Core · Live-code | 20 min |
| 4b | Retrieve + ground ARIA's answers | Core · Live-code | 20 min |
| — | Evaluate the RAG system | 🌱 Stretch · Self-paced | — |

## Learning objectives

- Understand **Retrieval-Augmented Generation (RAG)**: retrieve relevant text, then let the
  LLM answer *using only that text*
- Split documents into **chunks** and store them in a **vector database** (Chroma)
- Retrieve the most relevant chunks for a question
- Build a **grounded, citing** assistant — and see hallucinations disappear

## Why RAG

An LLM only knows what it was trained on. It doesn't know *Orbital's* specific procedures.
RAG bridges that gap: we find the right manual passages with embeddings (Module 2), then
hand them to the model as context. The model answers from **facts we control**.

## Prerequisites

- Ollama running with `nomic-embed-text` and `llama3.2`.
- The manuals in [`../data/manuals/`](../data/manuals/).

## Beats

### 4a · Chunk & embed → [`04a_embed_docs.ipynb`](04a_embed_docs.ipynb)
Load the five manuals, split them into sections, embed each section, and load them into a
Chroma collection.

### 4b · Retrieve & ground → [`04b_retrieve_ground.ipynb`](04b_retrieve_ground.ipynb)
Ask *"What do I do if O₂ drops in Module B?"* — retrieve the right passages and have ARIA
answer **from the manual, with a citation.** Then re-ask the part-number question from
Module 3 and watch ARIA correctly say it doesn't know.

### 🌱 Stretch · Evaluate → [`stretch_evaluation.ipynb`](stretch_evaluation.ipynb)
How do we *know* RAG is working? Measure retrieval quality on a small set of questions.

## ✅ Done when
ARIA answers the O₂ question citing `emergency-procedures.md` / `life-support.md`, and
declines to invent the part number. Solution in [`solution/`](solution/).
