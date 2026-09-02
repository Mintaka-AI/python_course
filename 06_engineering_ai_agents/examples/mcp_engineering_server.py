"""A local MCP server that exposes a tested engineering calculation."""
from mcp.server import MCPServer

from engineering_tools import calculate_stress

mcp = MCPServer("engineering-tools")


@mcp.tool()
def axial_stress(force_n: float, area_m2: float) -> dict[str, float | str]:
    """Calculate uniform axial stress from force in N and area in square metres."""
    return calculate_stress(force_n, area_m2)


@mcp.resource("engineering://limitations")
def limitations() -> str:
    """Return the educational and safety limitations of this server."""
    return "Educational calculations only; qualified engineering review is required."


@mcp.prompt()
def explain_result(result_json: str) -> str:
    """Create instructions for explaining a verified calculation result."""
    return f"Explain this verified result, including formula, units, and limitations: {result_json}"


if __name__ == "__main__":
    mcp.run()
