# Module 2 · From logs to embeddings 🔢

> **Story:** Orbital's crew leave short written logs after every shift. When something goes
> wrong, ARIA should be able to find *similar past events* — even when they're worded
> differently. That's what **embeddings** are for.

**Time:** ~25 min · **Beats:** 1 (**Core**)

| Beat | What you do | Type | Time |
|---|---|---|---|
| 2 | Embed crew logs & search by meaning | Core · Live-code | 25 min |

## Learning objectives

- Understand what an **embedding** is: text → a list of numbers (a vector)
- Use a local embedding model (`nomic-embed-text` via Ollama) to embed text
- Measure similarity between vectors with **cosine similarity**
- Build a tiny **semantic search** over the crew logs

## Why this matters

Keyword search fails when people use different words for the same thing ("O₂ falling" vs
"oxygen partial pressure dropping"). Embeddings place *similar meanings* close together in
vector space, so search works by **meaning**, not exact words. This is the engine behind
**RAG** (Module 4) and **agentic retrieval** (Module 5).

## Prerequisites

- Ollama running with `nomic-embed-text` pulled (done in setup).
- `data/crew_logs.jsonl` exists (`python data/generate_telemetry.py`).

## Beat

### 2 · Embeddings & semantic search → [`02_embeddings.ipynb`](02_embeddings.ipynb)
Embed all crew logs, then ask *"oxygen is dropping and CO₂ rising in Module B"* and watch
the most relevant past logs float to the top — including ones that never use those exact
words.

## 🌱 Stretch goals
- Compare the similarity of two hand-written sentences you choose.
- Try embedding with the small model and see if results change.

## ✅ Done when
Your search returns the CO₂-scrubber logs first for an O₂/CO₂ query. Solution in
[`solution/`](solution/).
