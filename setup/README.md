# ⚙️ Setup — do this BEFORE the workshop

This takes ~20–40 minutes, mostly download time. Please finish it **before** the day so we can start building right away. Everything runs **locally** — no accounts or API keys.

At the end you'll run `python setup/verify.py` and see all ✅.

---

## 1. Install Python 3.10+

Check what you have:

```bash
python --version    # or: python3 --version
```

If it's older than 3.10 (or missing), install from [python.org](https://www.python.org/downloads/) or your package manager.

## 2. Install Ollama (our local AI runtime)

Ollama runs language models on your own machine and exposes an OpenAI‑compatible API at `http://localhost:11434`.

- **macOS / Windows:** download the installer from [ollama.com/download](https://ollama.com/download).
- **Linux:**

  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

After installing, make sure the Ollama app/service is **running**, then verify:

```bash
ollama --version
```

## 3. Pull the three models

These are the models we use all day. Download sizes are roughly a few GB total — do this on a good connection.

```bash
ollama pull llama3.2          # chat + agents
ollama pull phi3.5            # small-model demo
ollama pull nomic-embed-text  # embeddings / RAG
```

Quick smoke test:

```bash
ollama run llama3.2 "Say hello from Mars in one sentence."
```

(Type `/bye` to exit.)

## 4. Create a virtual environment & install packages

From the repository root:

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

> 💡 Prefer a one‑shot install? Run `bash setup/bootstrap.sh` (macOS/Linux) or
> `setup/bootstrap.ps1` (Windows) — it pulls models, installs packages, generates the workshop
> data, and runs the verifier (Ollama must already be installed and running).

## 5. Generate the workshop data

The telemetry and crew-log files are generated from a script so the workshop stays reproducible
without committing generated outputs. From the repository root, run:

```bash
python data/generate_telemetry.py
```

You should see it write:

```text
data/telemetry.csv
data/crew_logs.jsonl
```

## 6. Verify everything

With the virtual environment active and Ollama running:

```bash
python setup/verify.py
```

You want to see:

```
✅ Python 3.10+
✅ Required packages importable
✅ Ollama reachable at http://localhost:11434
✅ Model available: llama3.2
✅ Model available: phi3.5
✅ Model available: nomic-embed-text
✅ Chat call succeeded
✅ Embedding call succeeded

🎉 All good — you're ready for AI in a Day!
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `Ollama not reachable` | Make sure the Ollama app/service is running. On Linux: `ollama serve` in a spare terminal. |
| `Model not found` | Re‑run the matching `ollama pull …` from step 3. |
| `ModuleNotFoundError` | Activate the virtual environment, then `pip install -r requirements.txt`. |
| Slow first response | The first call loads the model into memory; later calls are faster. |
| Low RAM / laptop struggling | Use `phi3.5` instead of `llama3.2` where noted — it's smaller. |

Still stuck? Bring your laptop a few minutes early and we'll help you get green.
