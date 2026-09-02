"""A local, deterministic engineering-agent pattern with no external services."""

import math


def calculate_pressure(force_n: float, area_m2: float) -> dict[str, float]:
    """Calculate pressure in Pa from validated SI inputs."""
    if not math.isfinite(force_n) or not math.isfinite(area_m2):
        raise ValueError("force_n and area_m2 must be finite numbers")
    if force_n < 0:
        raise ValueError("force_n must be zero or greater")
    if area_m2 <= 0:
        raise ValueError("area_m2 must be greater than zero")
    return {"pressure_pa": force_n / area_m2}


def choose_tool(request_text: str) -> str:
    """Choose from a fixed local allowlist based on simple request text."""
    if "pressure" in request_text.lower():
        return "calculate_pressure"
    raise ValueError("No allowed local tool matches the request")


def run_local_request(request_text: str, force_n: float, area_m2: float) -> str:
    """Plan in text, calculate deterministically, then format a report."""
    tool_name = choose_tool(request_text)
    allowed_tools = {"calculate_pressure": calculate_pressure}
    result = allowed_tools[tool_name](force_n, area_m2)
    return (
        f"Selected tool: {tool_name}\n"
        f"Inputs: force={force_n:.1f} N, area={area_m2:.4f} m²\n"
        f"Pressure: {result['pressure_pa']:.1f} Pa"
    )


def main() -> None:
    request = "Calculate the pressure on the support."
    print(run_local_request(request, force_n=12_000.0, area_m2=0.006))


if __name__ == "__main__":
    main()
