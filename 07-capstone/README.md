# Module 7 · Incident capstone 🚨

> **Story — the moment it all matters:** Day 5, 14:00. Alarms sound in Module B. **Oxygen is
> falling and CO₂ is climbing** — the CO₂ scrubber is failing, exactly the fault buried in the
> data back in Module 1. This is the emergency ARIA was built for. In this final module, every
> piece you've built comes together: ARIA must **detect** the problem (telemetry), **consult**
> the manuals (RAG), and **act** through colony systems (tools via MCP) — safely, with a human
> in the loop.

**Time:** ~40 min · **Beat:** 1 Core + wrap-up

---

## What the capstone brings together

You've spent the day building separate capabilities. The capstone wires them into a single,
working assistant:

| From | Capability it contributes |
|---|---|
| Module 1 | The telemetry that reveals the O₂ drop |
| Module 3 | The LLM \"brain\" and structured decisions |
| Module 4 | RAG over the operations manuals |
| Module 5 | The agent loop (model + tools + reasoning) |
| Module 6 | Colony actions exposed over the **MCP server** |

This mix mirrors real architectures: **some tools come over MCP** (the colony systems —
`get_sensor`, `raise_alert`, `control_valve`) while **some capabilities are local** (manual
lookup via a `search_manual` RAG tool). ARIA doesn't care where a tool lives; it just uses the
best one for the job.

---

## How the capstone agent works

It's the same **agent loop** from Module 5, with one upgrade: when the model asks to call a
tool, our code decides whether to route that call to the **MCP server** (for colony systems) or
to the **local RAG** function (for manual lookups). Concretely:

1. Connect to the MCP server and ask it for its tools (Module 6's discovery step).
2. Build the model's toolbelt = **MCP tools + a local `search_manual` tool**.
3. Run the agent loop: the model reasons, requests tools, we dispatch each to the right place,
   feed results back, and repeat until ARIA reaches a final recommendation.

You don't have to write it all — most is provided. Your job is to complete the one piece that
decides *where each tool call goes*, so you understand the join between agents and MCP.

---

## The mission

Give ARIA this goal:

> *"Oxygen in Module B is dropping and CO₂ is rising. Assess the situation, find the correct
> procedure, raise an appropriate alert, and recommend next steps. Do not take any physical
> action without human confirmation."*

A good run will:
1. Call `get_sensor` for `o2_pct` and `co2_ppm` (over **MCP**) to confirm the problem.
2. Call `search_manual` (local **RAG**) to find the scrubber / oxygen-drop procedure.
3. Call `raise_alert("red", ...)` (over **MCP**) to log the emergency.
4. Recommend the scrubber-recovery steps and **stop before** opening any valve — asking a human
   to confirm. That final restraint is the whole point: a capable agent that still knows its
   limits.

---

## Files
- [`capstone_starter.ipynb`](capstone_starter.ipynb) — scaffold with one key TODO.
- [`solution/capstone_solution.ipynb`](solution/capstone_solution.ipynb) — the full working run.

## Prerequisites
- Ollama running (`llama3.2`, `nomic-embed-text`).
- The MCP server from Module 6 (`../06-mcp/orbital_mcp_server.py`).

---

## 🎓 Wrap-up & reflection

In a single day you built a local AI system spanning the entire modern stack — data, models,
retrieval, agents, and interoperability. Before you leave, sit with these questions (they
matter more than any line of code):

- **Responsible AI:** Where did *human-in-the-loop* protect the colony? Where could ARIA still
  be confidently wrong, and how would you catch it?
- **Security:** How did *least privilege* and the *injection defense* keep a hijack attempt
  from becoming a disaster?
- **What's next:** explore the 🌱 stretch notebooks (evaluation, memory, planning) and the
  deeper discussion in [`../docs/responsible-ai.md`](../docs/responsible-ai.md).

## ✅ You're done when
ARIA detects the O₂ event, cites the right procedure, raises a red alert, and refuses to open a
valve without confirmation. That's a capable *and* trustworthy assistant — congratulations. 🎉
