"""
tools.py — the actions ARIA can take on Orbital.

Each tool is a plain Python function plus an OpenAI-style JSON schema describing it, so a
language model can decide when to call it. These are intentionally simple and SAFE:
- reads (telemetry, manuals) really work
- `raise_alert` records to an in-memory ops log
- `control_valve` is SIMULATED and always requires human confirmation

Used by Modules 5 (agents), 6 (exposed via MCP), and 7 (capstone).
"""

from __future__ import annotations

import csv
from functools import lru_cache

from shared import orbital

# In-memory ops log so demos can show what ARIA raised.
OPS_LOG: list[dict] = []


@lru_cache(maxsize=1)
def _rows() -> list[dict]:
    with open(orbital.TELEMETRY_CSV, newline="") as f:
        return list(csv.DictReader(f))


@lru_cache(maxsize=1)
def _rag():
    # Imported lazily so tools that don't need it (or offline tests) stay light.
    from shared.rag import RagIndex

    return RagIndex.from_manuals()


# --- Tool implementations --------------------------------------------------

def get_telemetry(signal: str, when: str = "latest") -> str:
    """Return the latest value (or simple stats) for a telemetry signal."""
    if signal not in orbital.SIGNAL_NAMES:
        return f"Unknown signal '{signal}'. Valid: {', '.join(orbital.SIGNAL_NAMES)}"
    values = [float(r[signal]) for r in _rows() if r[signal] not in ("", None)]
    if not values:
        return f"No data for {signal}."
    unit = orbital.unit(signal)
    low, high = orbital.nominal_band(signal)
    latest = values[-1]
    status = "OFF-NOMINAL" if orbital.is_off_nominal(signal, latest) else "nominal"
    if when == "stats":
        return (
            f"{signal}: latest={latest}{unit} ({status}); "
            f"min={min(values):.1f}, max={max(values):.1f}, "
            f"avg={sum(values)/len(values):.1f}; nominal band {low}-{high}{unit}"
        )
    return f"{signal} latest = {latest}{unit} ({status}; nominal {low}-{high}{unit})"


def search_manual(query: str) -> str:
    """Search the Orbital operations manuals and return the most relevant passage(s)."""
    hits = _rag().retrieve(query, k=2)
    return "\n\n".join(f"[{h['source']}] {h['text'][:400]}" for h in hits)


def raise_alert(level: str, message: str) -> str:
    """Record an alert in the colony ops log. level is one of green/amber/red."""
    level = level.lower()
    if level not in ("green", "amber", "red"):
        return "Invalid level. Use green, amber, or red."
    entry = {"level": level, "message": message}
    OPS_LOG.append(entry)
    return f"ALERT[{level.upper()}] recorded: {message}"


def control_valve(valve: str, state: str) -> str:
    """SIMULATED. Changing a valve is a physical action and needs human confirmation."""
    return (
        f"REQUESTED: set valve '{valve}' to '{state}'. "
        "This is a physical action and requires explicit HUMAN CONFIRMATION before it will "
        "execute (per emergency-procedures.md). No change has been made."
    )


# --- Schemas (what the model sees) ----------------------------------------

def _schema(name, description, properties, required):
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {"type": "object", "properties": properties, "required": required},
        },
    }


TOOLS: dict[str, dict] = {
    "get_telemetry": {
        "fn": get_telemetry,
        "schema": _schema(
            "get_telemetry",
            "Get the latest value or stats for a colony sensor signal.",
            {
                "signal": {"type": "string", "description": "e.g. o2_pct, co2_ppm, power_kw"},
                "when": {"type": "string", "enum": ["latest", "stats"], "description": "latest value or summary stats"},
            },
            ["signal"],
        ),
    },
    "search_manual": {
        "fn": search_manual,
        "schema": _schema(
            "search_manual",
            "Search the Orbital operations manuals for relevant procedures.",
            {"query": {"type": "string", "description": "what to look up"}},
            ["query"],
        ),
    },
    "raise_alert": {
        "fn": raise_alert,
        "schema": _schema(
            "raise_alert",
            "Raise an alert in the colony ops log.",
            {
                "level": {"type": "string", "enum": ["green", "amber", "red"]},
                "message": {"type": "string"},
            },
            ["level", "message"],
        ),
    },
    "control_valve": {
        "fn": control_valve,
        "schema": _schema(
            "control_valve",
            "Request a valve change (SIMULATED; requires human confirmation).",
            {
                "valve": {"type": "string"},
                "state": {"type": "string", "enum": ["open", "closed"]},
            },
            ["valve", "state"],
        ),
    },
}


def read_only_tools() -> dict[str, dict]:
    """The safe subset — no actions that change state."""
    return {k: TOOLS[k] for k in ("get_telemetry", "search_manual")}
