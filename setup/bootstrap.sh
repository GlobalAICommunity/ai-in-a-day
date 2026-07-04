#!/usr/bin/env bash
# AI in a Day — one-shot bootstrap (macOS / Linux).
# Assumes Python 3.10+ and Ollama are already installed and Ollama is running.
set -euo pipefail

echo "🛰️  AI in a Day — bootstrap"

# 1. Pull local models
for model in llama3.2 phi3.5 nomic-embed-text; do
  echo "→ Pulling $model ..."
  ollama pull "$model"
done

# 2. Virtual environment + dependencies
if [ ! -d ".venv" ]; then
  echo "→ Creating virtual environment (.venv) ..."
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3. Generate reproducible workshop data
python data/generate_telemetry.py

# 4. Verify
python setup/verify.py
