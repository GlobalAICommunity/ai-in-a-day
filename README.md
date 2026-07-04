# 🛰️ AI in a Day — *Orbital*

> Spend one day building the AI systems for **Orbital**, a fictional Mars research colony — and learn modern AI end‑to‑end, entirely on your own laptop.

**AI in a Day** is a hands‑on, 8‑hour workshop for people who know a little Python but are new to AI/ML. You'll build a colony assistant called **ARIA** and grow it across the day: from reading sensor data, to talking to a language model, to grounding it in the colony's manuals (RAG), to letting it take actions safely as an **agent**, to wiring it into real systems with the **Model Context Protocol (MCP)**.

Everything runs **locally and offline** using [Ollama](https://ollama.com) — **no cloud accounts, no API keys, no bills.**

---

## 🎯 What you'll learn

By the end of the day you will have hands‑on experience with:

- 📊 **Data & ML** — explore and clean colony telemetry, then train a model to flag anomalies
- 🔢 **Embeddings** — turn text into vectors and find similar incidents
- 🤖 **Generative AI & LLMs** — prompt a local model and build a chat assistant
- 📚 **RAG** — ground the assistant in the colony's operations manuals
- 🛠️ **AI Agents** — give the assistant tools so it can *act*, including multi‑agent teamwork
- 🔌 **MCP** — expose colony systems as tools through the Model Context Protocol
- 🛡️ **Responsible AI & security** — woven throughout: hallucinations, human‑in‑the‑loop, prompt injection

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

> Each module is split into short **beats** tagged **Core** (done together) or **Stretch** (optional / self‑paced). Fast groups do the stretch goals; everyone finishes the Core path.

---

## ✅ Before you arrive — REQUIRED pre‑work (~20–40 min)

The workshop starts *building*, not installing. Please complete setup **before** the day — the big model downloads take time on shared Wi‑Fi.

👉 **Follow [setup/README.md](setup/README.md)** to:

1. Install **Python 3.10+** and **Ollama**
2. Pull the local models: `llama3.2`, `phi3.5`, `nomic-embed-text`
3. Create a virtual environment and `pip install -r requirements.txt`
4. Run the verifier:

   ```bash
   python setup/verify.py
   ```

   You should see all green ✅. If you do, you're ready.

---

## 🚀 Running the workshop

- Work through the module folders in order: `01-data-and-ml/` → `07-capstone/`.
- Each folder has a **`README.md`** (the lesson) and **starter notebooks**. Full answers live in each module's **`solution/`** folder.
- Shared helpers live in [`shared/`](shared/); the colony's data and manuals live in [`data/`](data/).

### 👩‍🏫 For instructors

See [`docs/instructor-guide.md`](docs/instructor-guide.md) for per‑beat timing, talking points, what to live‑code vs. demo, and common pitfalls. A slide outline is in [`docs/slides-outline.md`](docs/slides-outline.md).

### 🧑‍💻 For self‑paced learners

Just start at [`01-data-and-ml/README.md`](01-data-and-ml/README.md) and go at your own speed. Do the **Stretch** beats whenever you like.

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
01-data-and-ml/ … 07-capstone/   The eight modules (lesson + starter + solution)
docs/         Instructor guide, slides outline, responsible-AI notes
```

---

## 🙏 Credits & inspiration

The **structure and pacing** of this workshop were inspired by Microsoft's excellent open‑source *"…for Beginners"* curricula (AI, ML, Data Science, Generative AI, AI Agents, and MCP). All scenario, data, prompts, and code in **AI in a Day** are original and written for this workshop.

## 📄 License

No separate license file is included yet. Add one before publishing the workshop outside your organization.