"""Ask OpenAI to explain a result calculated by deterministic Python code."""

import os

from openai import OpenAI


def calculate_stress_mpa(force_n: float, area_m2: float) -> float:
    """Return axial stress in MPa after validating the input domain."""
    if force_n < 0:
        raise ValueError("Force must not be negative.")
    if area_m2 <= 0:
        raise ValueError("Area must be greater than zero.")
    return force_n / area_m2 / 1_000_000


def main() -> None:
    """Calculate first, then request a beginner-friendly explanation."""
    force_n = 120_000.0
    area_m2 = 0.0008
    stress_mpa = calculate_stress_mpa(force_n, area_m2)

    verified_facts = f"""
Calculation: axial stress
Force: {force_n} N
Area: {area_m2} m²
Formula: stress = force / area
Verified result: {stress_mpa:.1f} MPa
Assumption: uniform axial force over the stated area
Limitation: educational example; no design approval
"""

    client = OpenAI()
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6"),
        instructions=(
            "Explain only the verified facts supplied by the application. "
            "Use three short bullet points for a beginner. Include the units and "
            "assumption. Do not recalculate, invent values, or claim design approval."
        ),
        input=verified_facts,
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
