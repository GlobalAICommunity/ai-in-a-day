"""
orbital_mcp_server.py — an MCP server exposing Orbital's colony systems as tools.

The Model Context Protocol (MCP) is a standard way to expose tools/data to AI apps. Any
MCP-aware client (Claude Desktop, VS Code, our own client in 06b, an agent) can connect and
call these tools — without knowing anything about our Python code.

Run it directly for a quick check:
    python 06-mcp/orbital_mcp_server.py        # (waits for an MCP client on stdio)

More usefully, a client launches it for you (see 06b_connect_client.ipynb).
"""

from __future__ import annotations

import os
import sys

# Make the repo root importable so we can reuse shared/ regardless of how we're launched.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from shared import orbital, tools  # noqa: E402

mcp = FastMCP("orbital")


@mcp.tool()
def get_sensor(signal: str) -> str:
    """Get the latest reading for a colony sensor (e.g. o2_pct, co2_ppm, power_kw)."""
    return tools.get_telemetry(signal, when="latest")


@mcp.tool()
def sensor_stats(signal: str) -> str:
    """Get summary statistics (min/max/avg + latest) for a colony sensor."""
    return tools.get_telemetry(signal, when="stats")


@mcp.tool()
def list_alerts() -> str:
    """List alerts currently recorded in the colony ops log."""
    if not tools.OPS_LOG:
        return "No alerts recorded."
    return "\n".join(f"[{a['level'].upper()}] {a['message']}" for a in tools.OPS_LOG)


@mcp.tool()
def raise_alert(level: str, message: str) -> str:
    """Raise an alert (green|amber|red) in the colony ops log."""
    return tools.raise_alert(level, message)


@mcp.tool()
def control_valve(valve: str, state: str) -> str:
    """SIMULATED. Request a valve change. Requires human confirmation; makes no real change."""
    return tools.control_valve(valve, state)


@mcp.resource("orbital://signals")
def signals() -> str:
    """The list of available telemetry signals and their nominal bands."""
    lines = [f"{name}: {lo}-{hi} {unit}" for name, (unit, lo, hi) in orbital.SIGNALS.items()]
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")
