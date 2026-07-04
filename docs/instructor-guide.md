# Instructor Guide — AI in a Day (*Orbital*)

This guide gives you per-module timing, talking points, what to **live-code** vs **demo**,
and common pitfalls. The workshop is designed to be run by an instructor **and** followed
self-paced, so every core lab has a full solution.

## Before the day

- Send attendees the [setup guide](../setup/README.md) at least a few days ahead. The model
  downloads are the #1 cause of a slow start. Make setup **mandatory pre-work**.
- Ask attendees to run `python setup/verify.py` and confirm all green.
- Have a backup plan for stragglers: a couple of spare machines, or pair them up.
- Test the whole flow yourself on the venue Wi-Fi if you can.

## Timing overview (~8 hours)

| Block | Module | Core time |
|---|---|---:|
| 09:00 | M0 Bootstrap check | 10 min |
| 09:10 | M1 Reading the colony's data | 50 min |
| 10:00 | ☕ Break | 15 min |
| 10:15 | M2 Embeddings | 25 min |
| 10:40 | M3 Meet ARIA | 70 min |
| 11:50 | 🍽️ Lunch | 45 min |
| 12:35 | M4 RAG | 40 min |
| 13:15 | M5 Agents | 70 min |
| 14:25 | ☕ Break | 15 min |
| 14:40 | M6 MCP | 50 min |
| 15:30 | M7 Capstone + wrap-up | 40 min |
| 16:10 | Buffer / stretch / Q&A | ~50 min |

The ~50 min buffer is deliberate — beginner rooms use it. Fast rooms spend it on 🌱 Stretch
beats.

## Per-module notes

### M0 · Bootstrap check (Demo, 10 min)
- Everyone runs `verify.py`. Fix red checks now; don't start M1 until most are green.
- Pitfall: Ollama not running. On Linux, `ollama serve` in a spare terminal.

### M1 · Data & ML (Live-code, 50 min)
- 1a: Emphasize *looking* at data before modeling. Ask "can you see the O₂ drop?" (Day 5).
- 1b: `IsolationForest` is unsupervised — stress it never saw the labels.
- Pitfall: `../data/telemetry.csv` missing → run `python data/generate_telemetry.py`.
- This is the least "AI-magic" module; keep energy up by tying it to the story.

### M2 · Embeddings (Live-code, 25 min)
- The "aha": search finds the scrubber logs for an O₂ query **without shared keywords**.
- Pitfall: first embed call is slow (model load). Warm it once before class.

### M3 · Meet ARIA (Demo+Live, 70 min)
- 3a: Run the temperature cell a few times so randomness is visible.
- 3b: The **hallucination demo** is the emotional core — let it invent a part number, then
  pause: "this is why we build RAG next." Don't rush it.
- 3c: Structured JSON output is the bridge to tools — call that out explicitly.

### M4 · RAG (Live-code, 40 min)
- Re-ask the part-number question and celebrate ARIA saying "I don't know."
- Pitfall: Chroma version differences — we pass our own embeddings, so no model download.

### M5 · Agents (Live-code, 70 min)
- 5a: Watch the printed tool trace — that *is* the agent reasoning.
- 5b: The **prompt-injection** beat is a highlight. Show the attack, then the defense
  (read-only tools + hardened prompt). Great discussion moment.
- 5c: Keep multi-agent simple: Engineer + Medic → Commander decides.
- Pitfall: smaller models sometimes skip tools. `llama3.2` is reliable; if a machine is slow,
  it's fine to demo from the front.

### M6 · MCP (Live-code, 50 min)
- Frame MCP as "the USB-C for AI tools." 6a shows the server; 6b connects a client.
- Pitfall: the client launches the server as a subprocess — paths matter. Notebooks use
  `os.path.abspath(...)` already.

### M7 · Capstone (40 min)
- This is the payoff: agent + MCP + RAG resolving the O₂ incident. Run the solution live if
  time is tight, then let attendees tweak the goal.
- End with the reflection questions in the module README.

## Facilitation tips
- Every beat is tagged **Core** or **Stretch**. When behind, drop Stretch, never Core.
- If a live call is slow, keep talking — the first call per model loads it into memory.
- Encourage pairs; debugging environments alone eats time.
- The solutions exist so a stuck attendee can peek and keep moving — that's allowed.
