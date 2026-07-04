# Slides Outline — AI in a Day (*Orbital*)

A lightweight deck outline. Keep slides sparse; the workshop lives in the notebooks. Aim for
a few slides per module, then get into the code.

## Opening (5 slides)
1. **Title** — AI in a Day: build the AI systems for the Orbital Mars colony.
2. **Why we're here** — go from "know a little Python" to shipping a modern AI system in a day.
3. **The rules** — everything runs locally (Ollama), no cloud, no keys.
4. **Meet Orbital & ARIA** — the scenario, the crew, the assistant we'll grow all day.
5. **The arc** — Data → Embeddings → LLMs → RAG → Agents → MCP → Capstone.

## M1 · Data & ML (3)
- What is telemetry; what is an anomaly.
- Explore → clean → visualize.
- Unsupervised anomaly detection in one slide (IsolationForest intuition).

## M2 · Embeddings (2)
- Words → vectors → "closeness = similar meaning."
- Why keyword search fails and embeddings win.

## M3 · Generative AI (4)
- What an LLM actually does (predicts plausible text).
- Tokens, temperature, message roles.
- Prompting: system prompt + few-shot.
- ⚠️ Hallucination — and why it's dangerous for life support.

## M4 · RAG (3)
- The problem: the model doesn't know *our* facts.
- Retrieve → ground → cite.
- Before/after: the part-number question.

## M5 · Agents (4)
- From "chatbot" to "agent": tools + a loop.
- The four Orbital tools.
- 🛡️ Prompt injection & least privilege.
- Multi-agent: specialists + a coordinator.

## M6 · MCP (3)
- MCP = "USB-C for AI tools."
- Client ↔ server; tools & resources.
- Security: validate, least privilege, human-in-the-loop.

## M7 · Capstone + close (3)
- The incident: O₂ drop in Module B.
- One picture: agent + MCP + RAG working together.
- Recap + where to go next (stretch notebooks, responsible-ai.md).

## Cross-cutting slides to sprinkle in
- **Responsible AI** reminder whenever ARIA gains a new power (M3, M5, M6).
- **Human-in-the-loop** whenever a physical action appears.
