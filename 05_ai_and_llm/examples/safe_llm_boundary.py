"""Offline example: validate model-like JSON before using it."""
import json
from typing import Any


def parse_explanation(raw_text: str) -> dict[str, Any]:
    data = json.loads(raw_text)
    if data.get("status") not in {"ok", "needs_input", "refused"}:
        raise ValueError("Unexpected status.")
    if not isinstance(data.get("explanation"), str):
        raise ValueError("Explanation must be text.")
    return data


def calculate_stress_pa(force_n: float, area_m2: float) -> float:
    if force_n < 0 or area_m2 <= 0:
        raise ValueError("Force must be non-negative and area must be positive.")
    return force_n / area_m2


stress_mpa = calculate_stress_pa(120_000, 0.0008) / 1_000_000
mock_response = json.dumps({"status": "ok", "explanation": f"Verified stress: {stress_mpa:.1f} MPa."})
print(parse_explanation(mock_response)["explanation"])
