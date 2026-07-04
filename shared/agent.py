"""
agent.py — a tiny, transparent tool-calling agent loop.

This is the whole idea of an "AI agent" in ~30 lines: give the model some tools, and let it
decide which to call, in what order, until it can answer. We keep it readable on purpose so
you can see exactly what's happening — no framework magic.

    from shared.agent import run_agent
    from shared.tools import TOOLS
    answer = run_agent("You are ARIA...", "Is O2 ok in Module B?", TOOLS)

Used by Module 5 (agents) and Module 7 (capstone).
"""

from __future__ import annotations

import json
from typing import Callable

from shared.llm import CHAT_MODEL, get_client


def run_agent(
    system: str,
    user: str,
    tools: dict[str, dict],
    *,
    model: str = CHAT_MODEL,
    max_steps: int = 6,
    verbose: bool = True,
    on_tool: Callable[[str, dict, str], None] | None = None,
) -> str:
    """
    Run the model with tools until it produces a final answer.

    `tools` maps name -> {"fn": callable, "schema": openai_tool_schema}.
    Returns the final assistant message text.
    """
    client = get_client()
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    tool_specs = [t["schema"] for t in tools.values()]

    for _step in range(max_steps):
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tool_specs,
            temperature=0,
        )
        msg = resp.choices[0].message

        # No tool calls -> the model is done.
        if not msg.tool_calls:
            return msg.content or ""

        # Record the assistant's tool-call request.
        messages.append(msg.model_dump(exclude_none=True))

        # Execute each requested tool and feed results back.
        for call in msg.tool_calls:
            name = call.function.name
            try:
                args = json.loads(call.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}

            if name not in tools:
                result = f"ERROR: unknown tool '{name}'"
            else:
                try:
                    result = str(tools[name]["fn"](**args))
                except Exception as exc:  # surface tool errors to the model
                    result = f"ERROR: {exc}"

            if verbose:
                print(f"  🛠️  {name}({args}) -> {result[:100]}")
            if on_tool:
                on_tool(name, args, result)

            messages.append(
                {"role": "tool", "tool_call_id": call.id, "content": result}
            )

    return "(stopped: reached max steps without a final answer)"
