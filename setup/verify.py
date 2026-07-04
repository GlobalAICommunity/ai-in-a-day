#!/usr/bin/env python3
"""
AI in a Day — setup verifier.

Checks that your machine is ready for the workshop:
  1. Python 3.10+
  2. Required packages import
  3. Ollama is reachable
  4. The three models are available
  5. A real chat call and embedding call succeed

Run:  python setup/verify.py
Everything is local — no internet or API keys required (once models are pulled).
"""

from __future__ import annotations

import sys
import urllib.error
import urllib.request

OLLAMA_URL = "http://localhost:11434"
REQUIRED_MODELS = ["llama3.2", "phi3.5", "nomic-embed-text"]
REQUIRED_PACKAGES = ["openai", "pandas", "numpy", "sklearn", "matplotlib", "chromadb", "mcp"]

OK = "✅"
BAD = "❌"
failures: list[str] = []


def check(label: str, passed: bool, hint: str = "") -> None:
    print(f"{OK if passed else BAD} {label}")
    if not passed:
        failures.append(f"{label}{' — ' + hint if hint else ''}")


def check_python() -> None:
    check("Python 3.10+", sys.version_info >= (3, 10), "install Python 3.10 or newer")


def check_packages() -> None:
    import importlib

    missing = []
    for pkg in REQUIRED_PACKAGES:
        try:
            importlib.import_module(pkg)
        except Exception:
            missing.append(pkg)
    check(
        "Required packages importable",
        not missing,
        f"missing: {', '.join(missing)} — run: pip install -r requirements.txt",
    )


def check_ollama_reachable() -> list[str]:
    """Return the list of installed model names, or [] if unreachable."""
    try:
        with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags", timeout=5) as resp:
            import json

            data = json.loads(resp.read().decode("utf-8"))
        names = [m.get("name", "") for m in data.get("models", [])]
        check(f"Ollama reachable at {OLLAMA_URL}", True)
        return names
    except (urllib.error.URLError, TimeoutError, ConnectionError):
        check(
            f"Ollama reachable at {OLLAMA_URL}",
            False,
            "start Ollama (app/service) or run 'ollama serve'",
        )
        return []


def check_models(installed: list[str]) -> None:
    # Ollama tags look like "llama3.2:latest"; match on the base name.
    bases = {n.split(":")[0] for n in installed}
    for model in REQUIRED_MODELS:
        check(f"Model available: {model}", model in bases, f"run: ollama pull {model}")


def check_chat() -> None:
    try:
        from openai import OpenAI

        client = OpenAI(base_url=f"{OLLAMA_URL}/v1", api_key="ollama")
        resp = client.chat.completions.create(
            model="llama3.2",
            messages=[{"role": "user", "content": "Reply with the single word: online"}],
            max_tokens=5,
        )
        ok = bool(resp.choices and resp.choices[0].message.content)
        check("Chat call succeeded", ok)
    except Exception as exc:  # noqa: BLE001 - surface any error to the learner
        check("Chat call succeeded", False, str(exc)[:120])


def check_embedding() -> None:
    try:
        from openai import OpenAI

        client = OpenAI(base_url=f"{OLLAMA_URL}/v1", api_key="ollama")
        resp = client.embeddings.create(model="nomic-embed-text", input="oxygen levels nominal")
        ok = bool(resp.data and resp.data[0].embedding)
        check("Embedding call succeeded", ok)
    except Exception as exc:  # noqa: BLE001
        check("Embedding call succeeded", False, str(exc)[:120])


def main() -> int:
    print("🛰️  AI in a Day — checking your setup...\n")
    check_python()
    check_packages()
    installed = check_ollama_reachable()
    if installed or True:  # still attempt model checks to give clear guidance
        check_models(installed)
    # Only attempt live calls if openai is importable and Ollama responded.
    if "openai" not in [f.split(" ")[0] for f in failures]:
        check_chat()
        check_embedding()

    print()
    if failures:
        print(f"{BAD} {len(failures)} check(s) need attention:\n")
        for f in failures:
            print(f"   - {f}")
        print("\nSee setup/README.md for help, then run this again.")
        return 1

    print("🎉 All good — you're ready for AI in a Day!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
