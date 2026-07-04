# 🛰️ AI in a Day — *Orbital*

> Spend one day building the AI systems for **Orbital**, a fictional Mars research colony — and learn modern AI end‑to‑end, entirely on your own laptop.

**AI in a Day** is a hands‑on, 8‑hour workshop that takes you from "I've written a little Python" all the way to "I understand and can build the core pieces of a modern AI system." You do **not** need to know anything about AI, machine learning, or data science coming in — every idea is explained from first principles, in plain language, before we touch any code. If a word might be unfamiliar, we stop and explain it the first time it shows up.

Across the day you'll build one continuous project instead of a pile of disconnected exercises: a colony assistant called **ARIA**. She starts as nothing at all, and by the end of the day she can read live sensors, search written procedures, reason about what to do, and safely carry out actions — with a human always in control of anything that matters. Concretely, you'll walk through this arc:

1. **Reading sensor data** — understanding the raw numbers a real system produces.
2. **Talking to a language model** — sending it text and getting text back, and understanding *why* that's powerful and *where* it can go wrong.
3. **Grounding it in real documents** (this is called **RAG**, short for Retrieval-Augmented Generation) — so ARIA answers from real manuals instead of guessing.
4. **Letting it take actions safely as an agent** — giving ARIA a controlled set of tools it can choose to use.
5. **Wiring those actions into real systems with the Model Context Protocol (MCP)** — an open standard that lets any AI application use the same tools.

Each step builds directly on the one before it, so by the time you reach the final capstone incident in Module 7, every piece will feel familiar rather than new.

After the one-time setup, every lab runs **locally**, meaning entirely on your own computer, using a free tool called [Ollama](https://ollama.com) that runs AI models on your machine instead of in the cloud. That means: **no cloud accounts, no API keys, no bills, and nothing you type ever leaves your laptop.**

---

## 🧭 New to programming or AI? Start here

This workshop assumes you can read and run a little Python (a `for` loop, calling a function, that sort of thing) — but assumes **zero** prior knowledge of AI, machine learning, or the specific tools we use. If any of the following words are unfamiliar, read this short glossary once before you begin; every term is also re-explained the first time it matters in each module.

| Term | Plain-language meaning |
|---|---|
| **Terminal / command line** | A text-based window where you type commands instead of clicking buttons. On Windows this is often called "PowerShell" or "Command Prompt"; on macOS/Linux it's usually called "Terminal." All the `bash`/`powershell` code blocks in this workshop are things you type there. |
| **Python** | The programming language every file in this workshop is written in. |
| **Package / library** | Ready-made code someone else wrote that you can reuse, instead of writing everything from scratch (e.g. `pandas` for spreadsheets, `openai` for talking to AI models). |
| **`pip` / `pip install`** | The tool that downloads and installs Python packages onto your computer. |
| **Virtual environment (venv)** | An isolated, private set of installed packages just for this project, so it doesn't clash with other Python projects on your machine. |
| **Jupyter notebook (`.ipynb`)** | A document that mixes explanatory text with runnable code **cells**. You click a cell and press ▶ (or Shift+Enter) to run just that piece of code and see its output immediately below it — this is how you'll do almost all the hands-on work today. |
| **JSON** | A simple, universal text format for structured data — basically nested lists and `{key: value}` pairs. You'll see it constantly, because it's how AI models, tools, and web APIs exchange information. |
| **API** | "Application Programming Interface" — a defined way for one piece of software to ask another piece of software to do something (e.g. "please generate a reply to this message"), usually over a network connection. |
| **Model** | Here, this means an **AI model**: a program that has learned patterns from huge amounts of data, and can use those patterns to do things like predict text, or judge whether a sensor value looks unusual. |

Don't worry about memorizing this table — just know it's here if a term ever feels unfamiliar. Every module also defines its *own* new vocabulary the moment it becomes relevant, so you're never expected to already know something before it's explained.

---

## 🎯 What you'll learn

By the end of the day you will have hands‑on experience with every layer of a modern AI system, built up one honest step at a time rather than handed to you as a black box:

- 📊 **Data & ML** — explore and clean colony telemetry (sensor readings collected automatically over time), then train a model that learns what "normal" looks like well enough to flag anomalies on its own
- 🔢 **Embeddings** — turn written text into lists of numbers that capture *meaning*, so a computer can find related notes even when they use completely different words
- 🤖 **Generative AI & LLMs** — send text to a local language model and get a reply back, understand exactly what's happening when you do that, and use it to build a real chat assistant
- 📚 **RAG** — ground the assistant's answers in the colony's actual operations manuals, so it stops guessing and starts *citing sources*, like an open-book exam instead of a bluff
- 🛠️ **AI Agents** — give the assistant a controlled set of tools so it can *act* on your behalf — checking a sensor, raising an alert — including a small team of specialist agents working together
- 🔌 **MCP** — expose the colony's systems as tools through the **Model Context Protocol**, an open standard that lets *any* AI application reuse the same tools without custom glue code
- 🛡️ **Responsible AI & security** — not a separate lecture, but a thread woven through every module: what to do about a model that sounds confident but is wrong (**hallucination**), why a human must stay in control of anything irreversible (**human‑in‑the‑loop**), and how to defend against hidden malicious instructions in data (**prompt injection**)

Each of these ideas is explained in its own module's `README.md` the moment you need it — you never need to look anything up elsewhere.

---

## 🗺️ The day at a glance

| # | Module | You build | Time |
|---|--------|-----------|-----:|
| 0 | Bootstrap check | Confirm your setup works | 10 min |
| 1 | Reading the colony's data | Explore telemetry + an anomaly model | 50 min |
| 2 | From logs to embeddings | Semantic search over crew logs | 25 min |
| 3 | Meet ARIA | A local chat assistant | 70 min |
| 4 | ARIA reads the manuals | Retrieval‑augmented answers (RAG) | 40 min |
| 5 | ARIA takes action | A tool‑using, multi‑agent ARIA | 70 min |
| 6 | Wiring the colony | An MCP server for colony systems | 50 min |
| 7 | Incident capstone | ARIA resolves an O₂ emergency | 40 min |

Plus **lunch** and **two breaks**. Total ≈ 8 hours.

Notice how each module's "you build" column reads almost like a sentence: explore data → search by meaning → talk to a model → ground it in facts → let it act → connect it to real systems → put it all together under pressure. That's not a coincidence — it's the same order a real AI project is usually built in, and by Module 7 you'll be combining everything from Modules 1–6 into one working assistant, not starting over.

> Each module is split into short **beats** — small, focused chunks of roughly 15–25 minutes — tagged **Core** (worked through together, live) or **Stretch** (optional, self‑paced, for when you're ahead or want to go deeper later). Fast groups do the Stretch goals during the day; everyone else can always come back to them afterwards. Nobody needs to finish Stretch content to say they completed the workshop.

---

## ✅ Before you arrive — REQUIRED pre‑work (~20–40 min)

The workshop starts *building*, not installing. Please complete setup **before** the day — package installs and model downloads need an internet connection and take time on shared Wi‑Fi, and every minute spent installing during the workshop is a minute not spent learning.

👉 **Follow [setup/README.md](setup/README.md)**, which walks you through, in order:

1. Installing **Python 3.10+** (the programming language everything is written in) and **Ollama** (the free tool that runs AI models on your own machine)
2. Pulling — meaning downloading, the same word `git` uses — the three local models: `llama3.2`, `phi3.5`, `nomic-embed-text`
3. Creating a virtual environment (an isolated set of Python packages just for this project) and installing this workshop's dependencies with `pip install -r requirements.txt`
4. Generating the workshop's practice data: `python data/generate_telemetry.py`
5. Running the verifier, a small script that checks every piece is in place:

   ```bash
   python setup/verify.py
   ```

   You should see all green ✅. If you do, you're ready — if not, `setup/README.md` has a troubleshooting table for the most common snags.

---

## 🚀 Running the workshop

- Work through the module folders in numeric order: `01-data-and-ml/` → `07-capstone/`. Each one assumes you've completed the ones before it, because ARIA (and the data/manuals she uses) carry over from module to module.
- Each folder has a **`README.md`** (the lesson — read this first, it explains the *why* before you touch any code) and one or more **starter notebooks** (where you do the hands-on work, with `# TODO` markers showing exactly what to fill in). Full working answers live in each module's **`solution/`** folder, in case you get stuck and want to compare or just keep moving.
- Shared helper code that multiple modules reuse lives in [`shared/`](shared/) (for example, the function that talks to the local AI model). The colony's synthetic sensor data and operations manuals live in [`data/`](data/). You generally won't need to edit these directories directly — the notebooks import from them.

### 👩‍🏫 For instructors

See [`docs/instructor-guide.md`](docs/instructor-guide.md) for per‑beat timing, talking points, what to live‑code vs. demo, and common pitfalls. A slide outline is in [`docs/slides-outline.md`](docs/slides-outline.md).

### 🧑‍💻 For self‑paced learners

Just start at [`01-data-and-ml/README.md`](01-data-and-ml/README.md) and go at your own speed — every explanation in this workshop was written assuming you might be reading it alone, with no instructor in the room, so nothing depends on someone else filling in the gaps out loud. Do the **Stretch** beats whenever you like, and feel free to re-read a section if a term doesn't click the first time; that's normal, not a sign you're behind.

---

## 🧰 Tech stack (all local)

| Purpose | Tool |
|---|---|
| Local LLM runtime | **Ollama** (OpenAI‑compatible API) |
| Chat / agents model | `llama3.2` |
| Small‑model demo | `phi3.5` |
| Embeddings | `nomic-embed-text` |
| Data / ML | pandas, numpy, matplotlib, scikit‑learn |
| Vector store | Chroma |
| Tooling protocol | MCP Python SDK |

---

## 📦 Repository layout

```
setup/        Pre-work install guide + verify.py
shared/       Small helpers (LLM client, scenario constants)
data/         Telemetry generator, crew logs, and the colony manuals
01-data-and-ml/ … 07-capstone/   The seven lesson modules (lesson + starter + solution)
docs/         Instructor guide, slides outline, responsible-AI notes
```

---

## ❓ Frequently asked questions

**"I've never used Jupyter notebooks before — is that a problem?"** No. A notebook is just a document made of cells; text cells explain things, code cells run Python. Click a code cell and press **Shift+Enter** to run it — its output (a table, a chart, some text) appears directly underneath. You'll pick it up within the first few minutes of Module 1.

**"What if my laptop is slow or low on RAM?"** Use `phi3.5` instead of `llama3.2` wherever a module mentions it — it's a smaller model that trades a little quality for a lot of speed. Every module notes where this swap makes sense.

**"What happens to my data?"** Nothing leaves your laptop. Ollama runs the AI models as a local program on your machine; there is no cloud account, no API key, and no network request to an outside company involved in any lab.

**"I got stuck on a TODO — is that OK?"** Yes, completely. Every starter notebook has a matching notebook in `solution/` with full working code. Peeking to get unstuck and keep moving is not cheating; it's how the workshop is designed to be used.

---

## 🙏 Credits & inspiration

The **structure and pacing** of this workshop were inspired by Microsoft's excellent open‑source *"…for Beginners"* curricula (AI, ML, Data Science, Generative AI, AI Agents, and MCP). All scenario, data, prompts, and code in **AI in a Day** are original and written for this workshop.

## 📄 License

No separate license file is included yet. Add one before publishing the workshop outside your organization.