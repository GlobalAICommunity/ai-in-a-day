# Instructor Guide — AI in a Day (*Orbital*)

This guide gives you per-module timing, talking points, what to **live-code** vs **demo**,
and common pitfalls. The workshop is designed to be run by an instructor **and** followed
self-paced, so every core lab has a full solution.

**How to use this guide:** read it once, start to finish, at least a day before you teach.
On the day itself, keep it open on a second screen and skim the relevant "Per-module notes"
entry a few minutes before each module starts. You don't need to memorize anything — the
goal of this guide is to save you from being surprised, not to script every word you say.

**If you're a co-instructor or TA** rather than the lead presenter: your main job during
Live-code beats is to circulate the room, not to watch the front. Watch for stuck hands,
red `verify.py` output, and people quietly falling behind — the lead instructor can't see
that from the front of the room while live-coding.

## Before the day

- Send attendees the [setup guide](../setup/README.md) at least a few days ahead. The model
  downloads are the #1 cause of a slow start. Make setup **mandatory pre‑work**.
- Ask attendees to run `python setup/verify.py` and confirm all green, ideally by replying to
  a confirmation email/message so you know who *hasn't* done it before the day starts.
- Have a backup plan for stragglers: a couple of spare machines with everything pre-installed,
  or pair them up with someone who's ready. Pairing also helps quieter attendees who might
  otherwise silently get stuck.
- Test the whole flow yourself on the venue Wi‑Fi if you can, at least once, end to end,
  in the days before the workshop — not the morning of.
- **Room/tech checklist:** projector or screen-share tested with an actual notebook open
  (not just a slide), power outlets reachable from every seat, and — if attendees are on
  shared venue Wi‑Fi — a plan for the fact that Ollama's model downloads (a few GB) will
  choke a weak connection. This is exactly why setup is pre-work and not done live.
- Print or screen-share this line prominently before you start: *"If `verify.py` isn't all
  green, raise your hand now — we fix that before Module 1, not during it."*

## If you're running this self-paced (no live instructor)

Everything above still applies except the live facilitation notes. A few adjustments:
- Tell learners explicitly, up front, that peeking at `solution/` when stuck is expected and
  encouraged, not a sign of failure — this is stated in every module README, but it's worth
  repeating out loud if you're introducing the workshop to a group even without live-teaching
  it.
- The "~50 min buffer" in the timing table below becomes far less relevant; self-paced
  learners should simply go at their own speed and treat the times as rough guidance, not a
  clock they're racing against.
- The **pitfalls** listed per module below are the most likely places a self-paced learner
  gets stuck with nobody to ask — consider pinning them somewhere visible (a shared doc, a
  chat channel) for a self-paced cohort.

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
beats. Don't announce the buffer as "free time" up front; frame it as "catch-up time" so
rooms that need it don't feel rushed, and rooms that don't need it feel like they earned
extra depth via Stretch.

## Per-module notes

Each entry below follows the same shape: what to say, what to watch for, and the pitfall most
likely to eat your time if you don't pre-empt it.

### M0 · Bootstrap check (Demo, 10 min)
- Everyone runs `verify.py`. Fix red checks now; don't start M1 until most are green.
- Say something like: *"This ten minutes now saves us an hour of debugging later — that's
  the whole reason setup was pre-work."*
- Pitfall: Ollama not running. On Linux, `ollama serve` in a spare terminal. On macOS/Windows,
  check the Ollama menu-bar/tray icon is present.
- Watch for: attendees who skipped pre-work entirely. Pair them with someone green rather
  than letting them try to catch up alone while the room moves on.

### M1 · Data & ML (Live-code, 50 min)
- 1a: Emphasize *looking* at data before modeling. Ask "can you see the O₂ drop?" (Day 5) —
  wait for someone to actually point at their own chart before moving on; this is the moment
  that hooks people into the story.
- 1b: `IsolationForest` is unsupervised — stress it never saw the labels. A common student
  question here is "then how does it know what's wrong?" — the answer is that it just learns
  what *most* points look like and flags what's structurally different, which is worth saying
  out loud even though the README covers it.
- Pitfall: `../data/telemetry.csv` missing → run `python data/generate_telemetry.py`.
- Pitfall: attendees who ran the generator multiple times will have identical data (it's
  seeded), so "my numbers don't match yours" shouldn't happen — if it does, check they're in
  the right working directory.
- This is the least "AI-magic" module; keep energy up by tying it to the story ("we're not
  ready to trust an AI with life support until we've earned the right by understanding the
  data ourselves").

### M2 · Embeddings (Live-code, 25 min)
- The "aha": search finds the scrubber logs for an O₂ query **without shared keywords**. Let
  that moment breathe — ask the room "which words do the query and the top result actually
  have in common?" and let them realize the answer is "almost none."
- Pitfall: first embed call is slow (model load). Warm it once before class by running the
  first cell yourself a few minutes before attendees start, so you know roughly how long to
  expect them to wait.
- Common question: "is this the same thing as ChatGPT search?" — yes, conceptually; this is
  the same core mechanism behind semantic search features in many products they've used.

### M3 · Meet ARIA (Demo+Live, 70 min)
- 3a: Run the temperature cell a few times so randomness is visible. Explicitly contrast
  `temperature=0` (same answer every time) against a higher value, since "it gives a different
  answer each time" surprises people who expect computers to be deterministic.
- 3b: The **hallucination demo** is the emotional core of the whole day — let it invent a part
  number, then pause: *"this is why we build RAG next."* Don't rush it, and don't let anyone
  brush past it as "the AI made a mistake" — reframe it as "the AI did exactly what it's
  designed to do: predict plausible text. It was never designed to know facts."
- 3c: Structured JSON output is the bridge to tools — call that out explicitly ("the exact
  same shape you just built by hand is what an *agent* generates automatically in Module 5").
- Pitfall: attendees confuse the `system` role with something the model "remembers" across
  separate conversations — clarify that a fresh chat with no history has no memory of a
  previous one at all.

### M4 · RAG (Live-code, 40 min)
- Re-ask the part-number question and celebrate ARIA saying "I don't know." This callback to
  Module 3 is the single best applause line in the whole workshop — don't skip it even if
  you're behind schedule.
- Pitfall: Chroma version differences — we pass our own embeddings, so no model download is
  needed at this step; if attendees see Chroma trying to download something, they likely
  passed raw text instead of embeddings to `collection.add(...)`.
- Common question: "why not just paste the whole manual into the prompt?" — the README covers
  this (context window limits + irrelevant text hurting quality), but it's worth restating
  out loud since it's a genuinely common instinct.

### M5 · Agents (Live-code, 70 min)
- 5a: Watch the printed tool trace — that *is* the agent reasoning, in full view. Point at a
  specific line in the printed output and narrate it: "see, it decided *on its own* to call
  `get_telemetry` here — nobody told it to."
- 5b: The **prompt-injection** beat is a highlight of the day. Show the attack landing first
  (let the room feel slightly alarmed), then the defense (read-only tools + hardened prompt).
  Great discussion moment — ask "where else in software have you seen 'never trust user
  input' before?" (SQL injection is a good bridge if anyone knows web development).
- 5c: Keep multi-agent simple: Engineer + Medic → Commander decides. Resist the urge to add a
  fourth agent live even if someone asks — that's exactly what the Stretch notebooks are for.
- Pitfall: smaller/quantized models sometimes skip tools entirely and just answer in prose.
  `llama3.2` is reliable for this; if a machine is slow or a model misbehaves, it's completely
  fine to demo from the front on your machine rather than debugging one laptop for ten minutes.

### M6 · MCP (Live-code, 50 min)
- Frame MCP as "the USB-C for AI tools" early and repeat the phrase — it's the single mental
  model that makes the rest of the module click. 6a shows the server; 6b connects a client.
- Pitfall: the client launches the server as a subprocess — paths matter. Notebooks use
  `os.path.abspath(...)` already, but if attendees copy code into a different working
  directory, the relative path can break; the fix is usually "run the notebook from its own
  folder" or check the abspath logic is intact.
- Common question: "is this specific to this workshop, or a real standard?" — real standard;
  worth mentioning it's used by tools like Claude Desktop and VS Code itself.

### M7 · Capstone (40 min)
- This is the payoff: agent + MCP + RAG resolving the O₂ incident, using nothing that wasn't
  built earlier in the day. Say this explicitly — attendees often don't realize until this
  moment that they already built every piece themselves.
- Run the solution live if time is tight, narrating each tool call as it happens, then let
  attendees tweak the goal on their own machines afterward (e.g. "what if the incident is a
  dust storm instead of an O₂ drop?").
- End with the reflection questions in the module README — these land much better as a short
  group discussion (2–3 minutes) than as a silent read.

## Facilitation tips
- Every beat is tagged **Core** or **Stretch**. When behind, drop Stretch, never Core.
- If a live call is slow, keep talking — the first call per model loads it into memory, and
  narrating *why* it's slow ("the model is loading into RAM right now") turns dead air into
  another teaching moment instead of an awkward pause.
- Encourage pairs; debugging environments alone eats time, and peer debugging is often faster
  than waiting for an instructor to reach every hand.
- The solutions exist so a stuck attendee can peek and keep moving — that's allowed, and
  worth saying out loud more than once during the day, since some attendees feel like peeking
  is "cheating" unless explicitly told otherwise.
- Keep a visible "parking lot" (a whiteboard, a shared doc) for interesting tangents and
  questions that go beyond today's scope — it lets you defer without dismissing them.

## After the day
- Point attendees back to the 🌱 Stretch notebooks and [`responsible-ai.md`](responsible-ai.md)
  for anything they didn't get to live.
- If you're collecting feedback, the most useful question to ask is which specific beat felt
  rushed or confusing — that's far more actionable than a general satisfaction score, and it
  directly improves your next run of this guide.
