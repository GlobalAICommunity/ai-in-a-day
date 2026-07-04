# ⚙️ Setup — do this BEFORE the workshop

This takes ~20–40 minutes, mostly download time. Please finish it **before** the day so we can start building right away. Everything runs **locally** — no accounts or API keys — which means once these downloads are done, you don't need an internet connection to do the labs themselves (only the one-time setup needs the internet).

This guide assumes you've never done anything like this before, so every step explains *what* you're doing and *why*, not just the command to type. If you've set up Python projects before, feel free to skim — but even experienced folks should still run steps 2 and 3, since Ollama and the models are specific to this workshop.

At the end you'll run `python setup/verify.py`, a small program we wrote that checks every piece is correctly in place, and see all ✅.

---

## 1. Install Python 3.10+

Python is the programming language every file in this workshop is written in. "3.10+" means "version 3.10 or newer."

Check what you already have by opening a **terminal** (a text window where you type commands — on Windows this is usually "PowerShell" or "Command Prompt"; on macOS/Linux it's usually called "Terminal") and running:

```bash
python --version    # or: python3 --version
```

If it's older than 3.10 (or the command isn't found at all), install Python from [python.org](https://www.python.org/downloads/) or your operating system's package manager.

## 2. Install Ollama (our local AI runtime)

Normally, talking to an AI language model means sending your text over the internet to a company's servers (like OpenAI or Anthropic), which costs money and requires an account with an API key (a secret password-like string that proves you're allowed to use their service). **Ollama** is a free program that instead downloads AI models and runs them directly on your own computer, and it exposes them through the same kind of interface (an **API**, or "Application Programming Interface" — a defined way for programs to talk to each other) that those cloud services use, at `http://localhost:11434` (that address just means "this same computer"). That's what lets this entire workshop run without any account or bill.

- **macOS / Windows:** download the installer from [ollama.com/download](https://ollama.com/download).
- **Linux:**

  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

After installing, make sure the Ollama app/service is **running** (it usually starts automatically and sits quietly in the background), then verify it's installed correctly:

```bash
ollama --version
```

## 3. Pull the three models

An AI model is, physically, a large file full of learned numbers. "Pulling" a model just means downloading that file onto your machine, the same idea as `git pull` downloading code — Ollama stores it once and reuses it for every future run. These are the three models we use all day, each for a different purpose:

```bash
ollama pull llama3.2          # our main "brain" — chat + agents (Modules 3, 5, 7)
ollama pull phi3.5            # a smaller, faster model for comparison (Module 3)
ollama pull nomic-embed-text  # turns text into numbers for search (Modules 2, 4)
```

Download sizes are roughly a few GB total — do this on a good connection, ideally the night before, not five minutes before the workshop starts.

Quick smoke test — this asks `llama3.2` to actually generate a reply, confirming the whole chain (Ollama + model + your machine) works end to end:

```bash
ollama run llama3.2 "Say hello from Mars in one sentence."
```

(Type `/bye` to exit back to your normal terminal prompt.)

## 4. Create a virtual environment & install packages

A **virtual environment** (often shortened to "venv") is a private, isolated folder of Python packages just for this project, so installing things here can never conflict with other Python projects on your computer, and you can delete it later with zero side effects. A **package** (also called a **library**) is ready-made code someone else wrote and shared, so you don't have to write everything from scratch — for example, `pandas` for working with spreadsheet-like data, or `openai` for talking to a language model. `pip` is the tool that downloads and installs packages; `requirements.txt` in this repository simply lists which packages, and which versions, this workshop needs.

From the repository root (the top-level `ai-in-a-day` folder):

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

After running the "activate" line, you should see `(.venv)` appear at the start of your terminal prompt — that's your confirmation the virtual environment is active. You'll need to run that activate command again anytime you open a fresh terminal to work on this workshop.

> 💡 Prefer a one‑shot install? Run `bash setup/bootstrap.sh` (macOS/Linux) or
> `setup/bootstrap.ps1` (Windows) — it pulls models, installs packages, generates the workshop
> data, and runs the verifier (Ollama must already be installed and running).

## 5. Generate the workshop data

The telemetry (sensor readings) and crew-log files you'll use all day are not stored directly in this repository — they're **generated** by a small Python script instead. We did this on purpose: it keeps the workshop reproducible (everyone gets the exact same data, with the exact same hidden incidents, every time) without bloating the repository with generated files. From the repository root, with your virtual environment active, run:

```bash
python data/generate_telemetry.py
```

You should see it print a confirmation and write two files:

```text
data/telemetry.csv
data/crew_logs.jsonl
```

If you ever delete these files by accident, or want a completely fresh copy, just run the same command again.

## 6. Verify everything

With the virtual environment active (you should see `(.venv)` in your prompt) and Ollama running in the background, run our verification script:

```bash
python setup/verify.py
```

It checks, one by one: your Python version, that all required packages import correctly, that Ollama is reachable, that all three models are pulled, and finally makes one real chat call and one real embedding call to prove the whole pipeline genuinely works end to end — not just that the pieces are installed. You want to see:

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

If anything shows a ❌ instead, don't worry — the message next to it tells you exactly what to fix, and the troubleshooting table below covers the most common cases.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `Ollama not reachable` | Make sure the Ollama app/service is running. On Linux: `ollama serve` in a spare terminal. |
| `Model not found` | Re‑run the matching `ollama pull …` from step 3. |
| `ModuleNotFoundError` | Activate the virtual environment (step 4), then `pip install -r requirements.txt`. |
| Slow first response | The first call loads the model into memory; later calls are faster. This is normal and not a sign anything is broken. |
| Low RAM / laptop struggling | Use `phi3.5` instead of `llama3.2` where noted — it's smaller and lighter on memory. |
| `command not found: python` (but you installed it) | Try `python3` instead of `python` — some systems only register the `python3` name. |

Still stuck? Bring your laptop a few minutes early and we'll help you get green.
