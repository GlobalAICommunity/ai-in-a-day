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
the logs for *"O₂ is falling."* A plain **keyword search** — the kind that just checks whether
the exact same words appear — would find **nothing**, because the two sentences share almost
no words, even though they mean the same thing. Keyword search matches *letters*, not
*meaning*.

Humans don't have this problem: we understand that "O₂ falling" and "oxygen pressure
dropping" are the same concern, without consciously thinking about it. We want to give the
computer that same ability, so it can search by what a sentence *means* rather than by which
exact words it happens to contain. That's exactly what embeddings provide, and it's the single
idea that makes almost every "smart search" and AI-assistant feature possible.

---

## The concept, explained carefully

### What is an embedding?
An **embedding** is a way of turning a piece of text into a **list of numbers** (called a
**vector**) such that *texts with similar meaning get similar numbers*. A special AI model —
an **embedding model** — reads the text and outputs, say, 768 numbers that together capture
its meaning. You don't design these numbers by hand; the model produces them, having learned
from vast amounts of text what tends to mean the same thing as what.

You can picture each vector as a **point in space** — admittedly a space with hundreds of
dimensions, which is impossible to truly visualize, but the 2D/3D intuition still holds up
well enough to reason about. Texts about oxygen problems cluster in one region; texts about
dust storms cluster in another. "Meaning" becomes "location," and "similar meaning" becomes
"nearby points." That's the whole trick.

> Analogy: think of placing books in a library. Instead of shelving by the exact title,
> imagine shelving by *topic*, so all the books about the same idea end up physically next to
> each other — even if their titles use different words. Embeddings shelve *sentences* that
> way, automatically, and instantly, for any text you give them.

### How do we measure "similar"?
Once each text is a vector (a point/direction in space), we measure similarity with **cosine
similarity** — a number between -1 and 1 that describes whether two vectors point in the same
direction, regardless of how "long" each vector is:
- **near 1** → very similar meaning,
- **near 0** → unrelated,
- **below 0** → opposite-ish.

We'll compute this ourselves from the raw numbers; it's just a short formula (multiply
matching positions together, add them up, divide by the vectors' lengths), and seeing exactly
how it works demystifies the whole "AI understands meaning" idea — underneath, it's ordinary
arithmetic on a list of numbers.

### Where does the embedding model run?
Locally! We use Ollama's `nomic-embed-text` model. No cloud, no keys — the same text-to-vector
magic that powers big search systems, running entirely on your laptop, with nothing you type
ever leaving your machine.

---

## Why this matters for the rest of the day

Embeddings are the foundation of two things you'll build later, and understanding them now is
what makes those modules feel obvious instead of magical:
- **RAG (Module 4)** — to answer a question, we first *embed the question*, then find the
  manual passages whose embeddings are closest, and feed those to the language model. That's
  the exact same "embed, then compare" pattern you're about to build here, just applied to
  operations manuals instead of crew logs.
- **Agentic retrieval (Module 5)** — ARIA will decide to search for relevant knowledge on its
  own, using this same mechanism, as one of several tools available to her.

Understand embeddings now, and those later modules will feel natural rather than like new
magic tricks.

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
