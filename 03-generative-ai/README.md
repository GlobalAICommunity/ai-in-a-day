# Module 3 · Meet ARIA 🤖

> **Story:** Time to bring **ARIA** to life. In this module you talk to a language model
> running entirely on your laptop, learn to steer it with prompts, and build the first
> version of the colony assistant.

**Time:** ~70 min · **Beats:** 3 (all **Core**)

| Beat | What you do | Type | Time |
|---|---|---|---|
| 3a | First LLM call + choosing a model | Core · Demo+Live | 20 min |
| 3b | Prompting + Responsible AI | Core · Live-code | 25 min |
| 3c | Build the ARIA chat app + structured output | Core · Live-code | 25 min |

## Learning objectives

- Make your first **local LLM** call through Ollama's OpenAI-compatible API
- Understand **tokens**, **temperature**, and the **system / user / assistant** message roles
- Choose between a bigger model (`llama3.2`) and a small one (`phi3.5`)
- Write effective **system prompts** and **few-shot** examples
- See **hallucination** first-hand and learn the **human-in-the-loop** rule
- Get **structured (JSON) output** — the bridge to tool-using agents in Module 5

## Prerequisites

- Ollama running with `llama3.2` and `phi3.5` pulled.
- We use the tiny helper in [`shared/llm.py`](../shared/llm.py) so you don't repeat boilerplate.

## Beats

### 3a · LLM basics & model selection → [`03a_llm_basics.ipynb`](03a_llm_basics.ipynb)
Your first `chat()` call, temperature experiments, and a speed/quality comparison between
`llama3.2` and the smaller `phi3.5` (which matters on a power-constrained colony!).

### 3b · Prompting & Responsible AI → [`03b_prompting.ipynb`](03b_prompting.ipynb)
Give ARIA a personality and rules with a **system prompt**, steer it with **few-shot**
examples, then watch it confidently make something up — and discuss why that's dangerous
for a life-support assistant.

### 3c · The ARIA chat app → [`03c_chat_app.ipynb`](03c_chat_app.ipynb)
Build a multi-turn chat that remembers the conversation, then make ARIA return a
**structured JSON** assessment (`severity`, `action`, `rationale`). This structure is
exactly what we'll turn into **tool calls** in Module 5.

## 🛡️ Responsible AI thread

LLMs *predict plausible text* — they don't *know* facts. For Orbital that means ARIA can
sound confident and still be wrong. The rules we adopt today and keep all day:
1. **Ground** answers in real data/manuals (Module 4).
2. **Human-in-the-loop** for any physical action (Modules 5–7).
3. **Never trust instructions hidden in data** (Module 5 security beat).

## ✅ Done when
ARIA holds a short conversation and returns a valid JSON assessment. Solutions in
[`solution/`](solution/).
