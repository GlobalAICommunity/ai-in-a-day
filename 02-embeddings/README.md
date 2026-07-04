# Module 2 · From logs to embeddings 🔢

> **Story so far:** In Module 1 you worked with *numbers* from sensors. But a lot of what
> keeps a colony safe is written in *words* — the short notes the crew leave after every
> shift. In this module you'll teach the computer to understand those words well enough to
> find related notes, even when they're phrased completely differently. This single idea —
> **embeddings** — is the quiet engine behind search, RAG, and much of modern AI.

**Time:** ~25 min · **Beats:** 1 (**Core**)

| Beat | What you do | Type | Time |
|---|---|---|---|
| 2 | Embed crew logs & search by meaning | Core · Live-code | 25 min |

---

## The problem embeddings solve

Suppose a crew member types: *"oxygen partial pressure is dropping."* Later, someone searches
the logs for *"O₂ is falling."* A plain **keyword search** would find **nothing** — the two
sentences share almost no words, even though they mean the same thing. Keyword search matches
*letters*, not *meaning*.

Humans don't have this problem: we understand that "O₂ falling" and "oxygen pressure
dropping" are the same concern. We want to give the computer that same ability. That's
exactly what embeddings provide.

---

## The concept, explained carefully

### What is an embedding?
An **embedding** is a way of turning a piece of text into a **list of numbers** (called a
**vector**) such that *texts with similar meaning get similar numbers*. A special AI model —
an **embedding model** — reads the text and outputs, say, 768 numbers that together capture
its meaning.

You can picture each vector as a **point in space**. Texts about oxygen problems cluster in
one region; texts about dust storms cluster in another. "Meaning" becomes "location," and
"similar meaning" becomes "nearby points." That's the whole trick.

> Analogy: think of placing books in a library. Instead of shelving by the exact title,
> imagine shelving by *topic*, so all the books about the same idea end up physically next to
> each other — even if their titles use different words. Embeddings shelve *sentences* that
> way, automatically.

### How do we measure "similar"?
Once each text is a vector (a point/direction in space), we measure similarity with **cosine
similarity** — a number between -1 and 1 that describes whether two vectors point in the same
direction:
- **near 1** → very similar meaning,
- **near 0** → unrelated,
- **below 0** → opposite-ish.

We'll compute this ourselves; it's just a short formula, and seeing it demystifies the whole
thing.

### Where does the embedding model run?
Locally! We use Ollama's `nomic-embed-text` model. No cloud, no keys — the same text-to-vector
magic that powers big search systems, running on your laptop.

---

## Why this matters for the rest of the day

Embeddings are the foundation of two things you'll build later:
- **RAG (Module 4)** — to answer a question, we first *embed the question*, then find the
  manual passages whose embeddings are closest, and feed those to the language model.
- **Agentic retrieval (Module 5)** — ARIA will decide to search for relevant knowledge on its
  own, using this same mechanism.

Understand embeddings now, and those later modules will feel natural.

---

## Prerequisites

- Ollama running with `nomic-embed-text` pulled (done in setup).
- `data/crew_logs.jsonl` exists — a set of short, realistic crew notes. If it's missing:
  `python data/generate_telemetry.py`.

## Beat

### 2 · Embeddings & semantic search → [`02_embeddings.ipynb`](02_embeddings.ipynb)
You'll embed every crew log, then ask *"oxygen is dropping and CO₂ rising in Module B"* and
watch the most relevant past notes rise to the top — **including ones that never use those
exact words.** That "it just understood me" moment is the point of the module.

## 🌱 Stretch goals
- Compare the cosine similarity of two sentences *you* write. How similar does the model think
  they are? Try to find two sentences that are worded differently but score high.
- Re-run a search but embed with a different model and see whether the ranking changes.

## ✅ You're done when
A search for an oxygen/CO₂ problem returns the CO₂-scrubber logs first — even though your
query and those logs don't share the same words. Solution in [`solution/`](solution/).
