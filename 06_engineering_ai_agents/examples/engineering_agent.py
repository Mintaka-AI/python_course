"""Offline, deterministic engineering-agent architecture example."""
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

from engineering_tools import TOOL_FUNCTIONS


def run_tool(tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if tool_name not in TOOL_FUNCTIONS:
        return {"status": "refused", "reason": "Unsupported calculation tool."}
    required = {"force_n", "area_m2"}
    missing = sorted(required - arguments.keys())
    if missing:
        return {"status": "needs_input", "missing": missing}
    try:
        result = TOOL_FUNCTIONS[tool_name](**arguments)
    except (TypeError, ValueError) as error:
        return {"status": "invalid_input", "reason": str(error)}
    return {"status": "ok", "tool": tool_name, "arguments": arguments, "result": result}


def main() -> None:
    event = run_tool("calculate_stress", {"force_n": 120_000.0, "area_m2": 0.0008})
    event["time"] = datetime.now(timezone.utc).isoformat()
    event["limitations"] = ["Educational result; qualified engineering review required."]
    output_path = Path(__file__).parent / "agent_log.json"
    output_path.write_text(json.dumps(event, indent=2), encoding="utf-8")
    print(json.dumps(event, indent=2))


if __name__ == "__main__":
    main()
