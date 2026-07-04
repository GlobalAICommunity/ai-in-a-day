# Slides Outline — AI in a Day (*Orbital*)

A lightweight deck outline. Keep slides sparse; the workshop lives in the notebooks. Aim for
a few slides per module, then get into the code. Each bullet below is a slide; the indented
*"say:"* line is a one-sentence cue for what you're actually saying while it's on screen —
not a script to read verbatim, just enough to jog your memory. Swap in your own delivery.

**Presenter tips:** don't read the slide text aloud — the room can already read. Use the slide
as a visual anchor while you talk *around* it. Get off the slide and into the notebook as fast
as you reasonably can; the deck exists to frame each module, not to replace it.

## Opening (5 slides)
1. **Title** — AI in a Day: build the AI systems for the Orbital Mars colony.
   - *say:* "Today you're not just learning about AI — you're building one, piece by piece."
2. **Why we're here** — go from "no AI/ML background required" to shipping a modern AI system
   in a day.
   - *say:* "Every concept gets explained before we use it — if a term is unfamiliar, that's
     expected, not a sign you're behind."
3. **The rules** — everything runs locally (Ollama), no cloud, no keys, nothing leaves your
   laptop.
   - *say:* "That also means: whatever you build today, you can keep running for free,
     forever, on this same laptop."
4. **Meet Orbital & ARIA** — the scenario, the crew, the assistant we'll grow all day.
   - *say:* "ARIA starts today knowing nothing. By 4pm she'll detect an emergency, look up the
     right procedure, and know when to stop and ask a human."
5. **The arc** — Data → Embeddings → LLMs → RAG → Agents → MCP → Capstone.
   - *say:* "Notice this is one sentence, not seven unrelated topics — each module is the next
     ingredient in the same recipe."

## M1 · Data & ML (3)
- What is telemetry; what is an anomaly.
  - *say:* "We're starting with the least 'AI-magic' module on purpose — every AI system
    stands on top of data, so we start by trusting our own eyes first."
- Explore → clean → visualize.
- Unsupervised anomaly detection in one slide (IsolationForest intuition: learns "normal,"
  flags what isn't, never sees the answer key).

## M2 · Embeddings (2)
- Words → vectors → "closeness = similar meaning."
  - *say:* "Two sentences with almost no words in common can still mean the same thing —
    watch what happens when we search by meaning instead of by letters."
- Why keyword search fails and embeddings win (live demo beats any slide here — keep this
  slide short and get to the notebook).

## M3 · Generative AI (4)
- What an LLM actually does (predicts plausible text, one token at a time — not a fact
  database, not a reasoning engine).
- Tokens, temperature, message roles (system / user / assistant).
- Prompting: system prompt + few-shot.
- ⚠️ Hallucination — and why it's dangerous for life support.
  - *say:* "Watch closely — it's about to sound completely confident while being completely
    wrong. That's not a bug we'll patch; it's what this module fixes with RAG next."

## M4 · RAG (3)
- The problem: the model doesn't know *our* facts (it only knows patterns in text it was
  trained on, which doesn't include Orbital's actual manuals).
- Retrieve → ground → cite.
- Before/after: the part-number question.
  - *say:* "Same question, same model — the only thing that changed is that this time we gave
    it the real manual first."

## M5 · Agents (4)
- From "chatbot" to "agent": tools + a loop.
  - *say:* "An agent isn't a smarter model — it's the same model, given the ability to ask us
    to run code on its behalf, and a loop that lets it try again with the result."
- The four Orbital tools (`get_telemetry`, `search_manual`, `raise_alert`, `control_valve`).
- 🛡️ Prompt injection & least privilege.
  - *say:* "This log entry is trying to hijack our agent right now — watch what our defenses
    do about it."
- Multi-agent: specialists + a coordinator (Engineer + Medic → Commander decides).

## M6 · MCP (3)
- MCP = "USB-C for AI tools."
  - *say:* "Before this, every AI app wired up every tool its own bespoke way. MCP is the one
    connector everything can agree on."
- Client ↔ server; tools & resources; talking over stdio (no network needed).
- Security: validate inputs, least privilege, human-in-the-loop — the same three habits from
  Module 5, now enforced at the protocol boundary.

## M7 · Capstone + close (3)
- The incident: O₂ drop in Module B — the same fault first seen, as raw numbers, in Module 1.
- One picture: agent + MCP + RAG working together, with a human still holding final say over
  anything irreversible.
- Recap + where to go next (stretch notebooks, responsible-ai.md).
  - *say:* "Everything ARIA just did, you built with your own hands today — nothing in that
    incident response was magic you didn't understand."

## Cross-cutting slides to sprinkle in
- **Responsible AI** reminder whenever ARIA gains a new power (M3, M5, M6).
- **Human-in-the-loop** whenever a physical action appears.
- Consider a single recurring "slide template" for both of the above — same layout, same
  icon, every time — so the room recognizes the cue instantly without needing to re-read it.
