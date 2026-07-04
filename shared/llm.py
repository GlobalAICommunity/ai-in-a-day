"""
llm.py — one tiny place for talking to the local model via Ollama.

Ollama exposes an OpenAI-compatible API at http://localhost:11434/v1, so we use the
standard `openai` SDK and just point it at localhost. No API key or cloud account is
needed (the api_key value is ignored by Ollama but the SDK requires *something*).

Used across Modules 3–7. Import the helpers you need:

    from shared.llm import chat, embed, get_client

    print(chat("Say hello from Mars."))
"""

from __future__ import annotations

from typing import Iterable

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover - guidance for learners
    raise ImportError(
        "The 'openai' package is required. Run: pip install -r requirements.txt"
    ) from exc

# Local Ollama defaults.
BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"  # placeholder; Ollama ignores it

CHAT_MODEL = "llama3.2"
SMALL_MODEL = "phi3.5"
EMBED_MODEL = "nomic-embed-text"

_client: "OpenAI | None" = None


def get_client() -> "OpenAI":
    """Return a shared OpenAI client pointed at the local Ollama server."""
    global _client
    if _client is None:
        _client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
    return _client


def chat(
    prompt: str,
    *,
    system: str | None = None,
    model: str = CHAT_MODEL,
    temperature: float = 0.7,
    messages: list[dict] | None = None,
) -> str:
    """
    Send a single prompt (or a full message list) and return the reply text.

    - Pass `prompt` for a quick one-shot question.
    - Pass `messages` (a list of {"role", "content"} dicts) for multi-turn chats;
      `prompt`/`system` are ignored in that case.
    """
    client = get_client()
    if messages is None:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def embed(texts: str | Iterable[str], *, model: str = EMBED_MODEL) -> list[list[float]]:
    """
    Turn text into embedding vectors.

    Accepts a single string or an iterable of strings; always returns a list of
    vectors (one per input), so callers can treat the output uniformly.
    """
    if isinstance(texts, str):
        inputs = [texts]
    else:
        inputs = list(texts)

    client = get_client()
    resp = client.embeddings.create(model=model, input=inputs)
    # Preserve input order.
    return [item.embedding for item in sorted(resp.data, key=lambda d: d.index)]
