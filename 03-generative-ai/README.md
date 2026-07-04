# Module 3 · Meet ARIA 🤖

> **Story so far:** You can read the colony's numbers (Module 1) and search its words
> (Module 2). Now we bring the star of the show online: **ARIA**, the colony's AI assistant.
> This is most people's favourite module, because it's where you finally *talk to an AI* —
> one running entirely on your own laptop. We'll go slowly and explain what's actually
> happening under the hood, because understanding it now makes Modules 4–7 click into place.

**Time:** ~70 min · **Beats:** 3 (all **Core**)

| Beat | What you do | Type | Time |
|---|---|---|---|
| 3a | First LLM call + choosing a model | Core · Demo+Live | 20 min |
| 3b | Prompting + Responsible AI | Core · Live-code | 25 min |
| 3c | Build the ARIA chat app + structured output | Core · Live-code | 25 min |

---

## What *is* a large language model?

A **large language model** (**LLM**) is an AI trained on an enormous amount of text. Its one
and only skill is deceptively simple: **given some text, predict what comes next.** That's it.
Type "The capital of France is", and it predicts "Paris" because that's what usually follows.

From that single ability — predicting the next chunk of text, over and over — comes the
appearance of answering questions, writing code, summarising, and chatting. It's important to
sit with this: an LLM is a spectacularly good **text predictor**, not a database of verified
facts and not a reasoning engine that "knows" things. This is *why* it can sound completely
confident and still be wrong — a behaviour called **hallucination** that we'll meet head-on in
beat 3b, and defend against in Module 4.

### A few terms you'll hear all day

- **Token** — LLMs don't read whole words; they read **tokens**, which are word-pieces (\"oxy\",
  \"gen\"). A rough rule of thumb: one token ≈ ¾ of a word. Models have a limit on how many
  tokens they can consider at once (the **context window**).
- **Prompt** — the text you send to the model. Prompting well is a real skill (beat 3b).
- **Temperature** — a dial from 0 upward that controls randomness. Low temperature = focused
  and repeatable; high temperature = creative and varied (beat 3a).
- **Roles** — a chat is a list of messages, each with a role: **system** (hidden instructions
  that set the AI's behaviour), **user** (what the person says), and **assistant** (what the
  AI replies). You'll use all three.

---

## How we talk to the model (no cloud, no keys)

We run the model with **Ollama**, which serves it on your machine and, helpfully, speaks the
same API \"language\" as OpenAI. That means we can use the standard `openai` Python library but
point it at `http://localhost:11434` — your laptop — instead of the cloud.

You won't write that plumbing yourself. We wrapped it in a tiny helper,
[`shared/llm.py`](../shared/llm.py), which gives you two friendly functions:

```python
from shared.llm import chat, embed
chat(\"Say hello from Mars.\")     # returns the model's reply as a string
```

Keeping the boilerplate in one place lets you focus on the ideas, not the setup.

---

## Beats

### 3a · LLM basics & model selection → [`03a_llm_basics.ipynb`](03a_llm_basics.ipynb)
Make your first local LLM call, feel how **temperature** changes the output, and compare a
bigger model (`llama3.2`) with a smaller, faster one (`phi3.5`). On a power-limited colony,
choosing the *right-sized* model is a real engineering decision, not just \"bigger is better.\"

### 3b · Prompting & Responsible AI → [`03b_prompting.ipynb`](03b_prompting.ipynb)
Learn to steer the model. You'll give ARIA an identity and safety rules with a **system
prompt**, teach it a response format with **few-shot examples**, and then deliberately trigger
a **hallucination** so you understand — viscerally — why we never let an ungrounded LLM near a
life-support decision.

### 3c · The ARIA chat app + structured output → [`03c_chat_app.ipynb`](03c_chat_app.ipynb)
Build a real multi-turn conversation that *remembers* what was said, then make ARIA return a
**structured JSON** assessment (`severity`, `action`, `rationale`). That structured output is
the precise bridge to Module 5, where structured requests become **tool calls** an agent can
act on.

---

## 🛡️ The Responsible-AI thread starts here

Because an LLM predicts plausible text rather than truth, we adopt three rules today and keep
them for the rest of the workshop:
1. **Ground** answers in real data and documents (Module 4 makes this concrete).
2. Keep a **human in the loop** for any physical action (Modules 5–7).
3. **Never trust instructions hidden inside data** (Module 5's security beat).

## ✅ You're done when
ARIA can hold a short conversation *and* return a valid JSON assessment of a sensor reading.
Solutions are in [`solution/`](solution/) if you need them.
