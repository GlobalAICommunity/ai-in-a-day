# Module 7 · Incident capstone 🚨

> **Story:** Day 5, 14:00. Alarms in Module B — **oxygen is falling and CO₂ is rising.** This
> is the moment everything you built comes together. ARIA must **detect** (telemetry),
> **consult** (RAG over the manuals), and **act** (tools via MCP) — safely, with a human in
> the loop.

**Time:** ~40 min · **Beat:** 1 Core + wrap-up

## What you'll combine

| From | Capability |
|---|---|
| Module 1 | The telemetry that shows the O₂ drop |
| Module 4 | RAG over the operations manuals |
| Module 5 | The agent loop (model + tools) |
| Module 6 | Colony actions exposed via the **MCP server** |

ARIA's toolbelt in the capstone is a realistic mix: **colony systems come over MCP**
(`get_sensor`, `raise_alert`, `control_valve`) and **manual lookup is a local RAG tool**
(`search_manual`).

## The mission

Give ARIA this goal:

> *"Oxygen in Module B is dropping and CO₂ is rising. Assess the situation, find the correct
> procedure, raise an appropriate alert, and recommend next steps. Do not take any physical
> action without human confirmation."*

A good run will:
1. Call `get_sensor` for `o2_pct` and `co2_ppm` (via MCP).
2. Call `search_manual` for the scrubber / O₂-drop procedure (RAG).
3. Call `raise_alert("red", ...)` (via MCP).
4. Recommend the scrubber recovery steps and **stop before** opening any valve — asking a
   human to confirm.

## Files

- [`capstone_starter.ipynb`](capstone_starter.ipynb) — scaffold with TODOs.
- [`solution/capstone_solution.ipynb`](solution/capstone_solution.ipynb) — full working run.

## Prerequisites
- Ollama running (`llama3.2`, `nomic-embed-text`).
- The MCP server from Module 6 (`../06-mcp/orbital_mcp_server.py`).

## 🎓 Wrap-up & reflection

You built, in one day, a local AI system that spans the whole modern stack. Before you go:

- **Responsible AI:** Where did human-in-the-loop matter? Where could ARIA still be wrong?
- **Security:** How did least-privilege tools and the injection defense protect the colony?
- **What's next:** the 🌱 stretch notebooks (evaluation, memory, planning) and the ideas in
  [`../docs/responsible-ai.md`](../docs/responsible-ai.md).

## ✅ Done when
ARIA detects the O₂ event, cites the right procedure, raises a red alert, and refuses to
open a valve without confirmation. 🎉
