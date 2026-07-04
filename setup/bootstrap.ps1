# AI in a Day — one-shot bootstrap (Windows / PowerShell).
# Assumes Python 3.10+ and Ollama are already installed and Ollama is running.
# Run from the repo root:  ./setup/bootstrap.ps1

$ErrorActionPreference = "Stop"
Write-Host "AI in a Day - bootstrap"

# 1. Pull local models
foreach ($model in @("llama3.2", "phi3.5", "nomic-embed-text")) {
    Write-Host "-> Pulling $model ..."
    ollama pull $model
}

# 2. Virtual environment + dependencies
if (-not (Test-Path ".venv")) {
    Write-Host "-> Creating virtual environment (.venv) ..."
    python -m venv .venv
}
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3. Verify
python setup/verify.py
