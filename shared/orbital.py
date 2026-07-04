"""
Orbital — shared scenario constants and small helpers.

"Orbital" is a fictional Mars research colony. Every module in this workshop uses
the same names, signals, and thresholds defined here so the story stays consistent.

Nothing in here talks to an LLM — see shared/llm.py for that.
"""

from __future__ import annotations

from pathlib import Path

# --- Paths -----------------------------------------------------------------
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TELEMETRY_CSV = DATA_DIR / "telemetry.csv"
CREW_LOGS = DATA_DIR / "crew_logs.jsonl"
MANUALS_DIR = DATA_DIR / "manuals"

# --- The colony ------------------------------------------------------------
COLONY_NAME = "Orbital"
ASSISTANT_NAME = "ARIA"  # Autonomous Research & Infrastructure Assistant
MODULES = ["A", "B", "C", "Hab", "Lab", "EVA-Bay"]

# Crew roles used in the multi-agent module.
CREW_ROLES = ["Engineer", "Medic", "Commander"]

# --- Telemetry signals -----------------------------------------------------
# Each signal: (unit, nominal_low, nominal_high). Readings outside the nominal
# band are "off-nominal" and may indicate a problem.
SIGNALS: dict[str, tuple[str, float, float]] = {
    "habitat_temp_c": ("°C", 18.0, 26.0),
    "o2_pct": ("%", 19.5, 23.5),
    "co2_ppm": ("ppm", 400.0, 1000.0),
    "power_kw": ("kW", 30.0, 90.0),
    "battery_pct": ("%", 40.0, 100.0),
    "dust_index": ("AQI", 0.0, 150.0),
    "water_l": ("L", 800.0, 2000.0),
}

# Convenience: just the signal column names, in order.
SIGNAL_NAMES = list(SIGNALS.keys())


def is_off_nominal(signal: str, value: float) -> bool:
    """Return True if a reading is outside its nominal band."""
    if signal not in SIGNALS:
        raise KeyError(f"Unknown signal: {signal!r}")
    _unit, low, high = SIGNALS[signal]
    return value < low or value > high


def nominal_band(signal: str) -> tuple[float, float]:
    """Return (low, high) nominal band for a signal."""
    _unit, low, high = SIGNALS[signal]
    return low, high


def unit(signal: str) -> str:
    """Return the unit string for a signal."""
    return SIGNALS[signal][0]
