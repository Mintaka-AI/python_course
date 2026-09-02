"""A small OpenAI Responses API agent with one allowlisted Python tool."""
import json
import os
from typing import Any

from openai import OpenAI

from engineering_tools import TOOL_FUNCTIONS

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6")
MAX_TOOL_ROUNDS = 4

TOOLS = [
    {
        "type": "function",
        "name": "calculate_stress",
        "description": "Calculate uniform axial stress from force in N and area in m^2.",
        "parameters": {
            "type": "object",
            "properties": {
                "force_n": {"type": "number", "minimum": 0},
                "area_m2": {"type": "number", "exclusiveMinimum": 0},
            },
            "required": ["force_n", "area_m2"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]


def execute_tool(name: str, arguments_json: str) -> str:
    """Validate the tool name, parse arguments, and return JSON to the model."""
    if name not in TOOL_FUNCTIONS:
        return json.dumps({"status": "refused", "reason": "Unknown tool"})
    try:
        arguments: dict[str, Any] = json.loads(arguments_json)
        result = TOOL_FUNCTIONS[name](**arguments)
        return json.dumps({"status": "ok", "result": result})
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        return json.dumps({"status": "invalid_input", "reason": str(error)})


def run_agent(user_request: str) -> str:
    """Run a bounded model-tool-model loop and return the final explanation."""
    client = OpenAI()
    conversation: list[Any] = [{"role": "user", "content": user_request}]

    for _ in range(MAX_TOOL_ROUNDS):
        response = client.responses.create(
            model=MODEL,
            instructions=(
                "You are an educational engineering assistant. Use only the declared "
                "tool for numerical stress calculations. Never invent missing values or units. "
                "State the formula, units, assumptions, and educational limitation."
            ),
            tools=TOOLS,
            input=conversation,
        )
        conversation += response.output
        tool_calls = [item for item in response.output if item.type == "function_call"]
        if not tool_calls:
            return response.output_text

        for call in tool_calls:
            conversation.append(
                {
                    "type": "function_call_output",
                    "call_id": call.call_id,
                    "output": execute_tool(call.name, call.arguments),
                }
            )

    raise RuntimeError("The agent exceeded the allowed number of tool rounds")


if __name__ == "__main__":
    print(run_agent("Find the stress for 120000 N acting on 0.0008 m^2."))
