# Module 6 · Wiring the colony (MCP) 🔌

> **Story so far:** ARIA's tools currently live *inside our Python code*. Only our program can
> call them. But imagine you want to use those same colony tools from VS Code, or from a
> different assistant, or from a dashboard the crew builds next year. Rewriting the tools for
> every app would be madness. Instead we expose them **once** through a shared standard: the
> **Model Context Protocol (MCP)**. Think of MCP as the *USB-C port* for AI tools — one
> connector everything can plug into.

**Time:** ~50 min · **Beats:** 2 (both **Core**)

| Beat | What you do | Type | Time |
|---|---|---|---|
| 6a | Build an MCP server for colony systems | Core · Live-code | 25 min |
| 6b | Connect a client + MCP security | Core · Live-code | 25 min |

---

## What is MCP, and why should you care?

**MCP (Model Context Protocol)** is an open standard — an agreed-upon set of rules that
different programs follow so they can talk to each other reliably — for connecting AI
applications to tools and data. It defines a common "language" so that any AI app (a
**client**) can discover and use the capabilities offered by any tool provider (a **server**)
— without custom, one-off glue code for each combination of "this AI app" plus "that tool."

Before MCP, every AI app integrated every tool in its own bespoke way — if you have N AI apps
and M tools, that's potentially N×M different integrations, each maintained separately. MCP
turns that into N+M: build a tool as an MCP **server** once, and *every* MCP-aware client can
use it, and build a client once, and it can use *every* MCP server, without either side needing
to know the other's internal code. This is why MCP has been adopted across the industry
surprisingly fast: it's the plumbing that lets the AI ecosystem interoperate, the same way USB
let any peripheral plug into any computer once both sides agreed on one standard.

### The two roles
- **MCP server** — a program that *offers* capabilities. Ours (`orbital_mcp_server.py`) offers
  colony tools like reading a sensor or raising an alert. A server doesn't know or care who its
  clients are; it just answers requests according to the protocol.
- **MCP client** — a program that *uses* those capabilities. In 6b you'll write a client; in
  real life VS Code, Claude Desktop, or an agent framework could be the client, connecting to
  the exact same server you're about to build without any changes to it.

They talk over a **transport** — the underlying communication channel. We use **stdio**
("standard input/output," the same input/output channel a command-line program normally uses
to print text and read keyboard input): the client launches the server as a **subprocess** (a
program started and controlled by another program) and they exchange structured messages
through the pipe connecting them. Simple, entirely local, no network involved.

### Tools vs resources
MCP servers can expose two kinds of things:
- **Tools** — actions the client can *invoke*, i.e. functions it can call with arguments and
  get a result back (e.g. `get_sensor`, `raise_alert`).
- **Resources** — data the client can simply *read*, more like a file or a webpage than a
  function call (e.g. `orbital://signals`, the list of valid signals). Think tools = verbs,
  resources = nouns.

---

## Our server at a glance

[`orbital_mcp_server.py`](orbital_mcp_server.py) exposes:

| Tool | Purpose |
|---|---|
| `get_sensor(signal)` | latest reading for a signal |
| `sensor_stats(signal)` | min/max/avg + latest |
| `list_alerts()` | current ops-log alerts |
| `raise_alert(level, message)` | record an alert |
| `control_valve(valve, state)` | **simulated**, needs human confirmation |

Plus a **resource** `orbital://signals` listing valid signals and their nominal bands. Under
the hood these reuse the exact same functions from [`../shared/tools.py`](../shared/tools.py)
that your agent used in Module 5 — we're just publishing them over a standard protocol now.

---

## Beats

### 6a · Build the server → [`06a_build_server.ipynb`](06a_build_server.ipynb)
See how a plain Python function becomes an MCP tool with a single `@mcp.tool()` decorator, and
inspect everything the server offers. You'll appreciate how little code MCP requires.

### 6b · Connect a client → [`06b_connect_client.ipynb`](06b_connect_client.ipynb)
Act as an MCP client: launch the server, discover its tools over the protocol, call them, and
confirm the safety guard on `control_valve`. Then we discuss what makes an MCP server safe.

---

## 🛡️ MCP security (why this matters)

An MCP server is a door into your systems, so it must be built defensively:
- **Validate inputs** — never trust arguments blindly. Our `get_sensor` rejects unknown signal
  names; `raise_alert` only accepts valid levels.
- **Least privilege** — expose only what's needed, and keep dangerous actions simulated or
  guarded.
- **Human-in-the-loop** — `control_valve` only *requests* a change and returns a "needs human
  confirmation" message; it never actuates anything by itself.

## ✅ You're done when
Your client lists the five tools and successfully calls `get_sensor("o2_pct")` over MCP.
Solution in [`solution/`](solution/).
