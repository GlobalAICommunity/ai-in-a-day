# Module 6 · Wiring the colony (MCP) 🔌

> **Story:** ARIA's tools currently live inside our Python code. To make them reusable by
> *any* AI app — VS Code, another agent, a future dashboard — we expose them through the
> **Model Context Protocol (MCP)**, the "USB port" for AI tools.

**Time:** ~50 min · **Beats:** 2 (both **Core**)

| Beat | What you do | Type | Time |
|---|---|---|---|
| 6a | Build an MCP server for colony systems | Core · Live-code | 25 min |
| 6b | Connect a client + MCP security | Core · Live-code | 25 min |

## Learning objectives

- Understand **MCP**: a standard protocol so AI apps and tools can talk to each other
- Know the **client ↔ server** model and the difference between **tools** and **resources**
- Build an MCP **server** that exposes Orbital's systems
- Connect an MCP **client** and call the tools
- Apply MCP **security**: input validation, least privilege, human confirmation

## Why MCP

In Module 5, ARIA's tools were Python functions only *our* code could call. MCP turns them
into a **standard service**: define a tool once, and any MCP-aware client can use it. It's
how modern AI tools plug into editors, agents, and assistants without custom glue.

```
   ARIA / VS Code / any agent            our Python
        (MCP client)   <── stdio ──>   (MCP server: orbital_mcp_server.py)
```

## The server

[`orbital_mcp_server.py`](orbital_mcp_server.py) exposes:

| Tool | Purpose |
|---|---|
| `get_sensor(signal)` | latest reading for a signal |
| `sensor_stats(signal)` | min/max/avg + latest |
| `list_alerts()` | current ops-log alerts |
| `raise_alert(level, message)` | record an alert |
| `control_valve(valve, state)` | **simulated**, needs human confirmation |

Plus a **resource** `orbital://signals` listing valid signals and their nominal bands.

## Beats

### 6a · Build the server → [`06a_build_server.ipynb`](06a_build_server.ipynb)
Walk through the server code, see how a plain function becomes an MCP tool with `@mcp.tool()`,
and list what it exposes.

### 6b · Connect a client → [`06b_connect_client.ipynb`](06b_connect_client.ipynb)
Launch the server, connect an MCP client, discover the tools, and call them — then discuss
what could go wrong and how MCP servers stay safe.

## 🛡️ MCP security thread

- **Validate inputs** — a tool must never trust arguments blindly (our `get_sensor` checks
  the signal name; `raise_alert` checks the level).
- **Least privilege** — expose only what's needed; keep dangerous actions simulated/guarded.
- **Human-in-the-loop** — `control_valve` only *requests*; a human confirms real actions.

## ✅ Done when
Your client lists the five tools and successfully calls `get_sensor("o2_pct")`. Solution in
[`solution/`](solution/).
