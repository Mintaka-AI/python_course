"""Auditable axial-stress calculator using only the standard library."""
from datetime import datetime, timezone
import json
from pathlib import Path


def calculate_stress_pa(force_n: float, area_m2: float) -> float:
    """Return axial stress in Pa for a uniform force over a positive area."""
    if force_n < 0:
        raise ValueError("Force must not be negative.")
    if area_m2 <= 0:
        raise ValueError("Area must be greater than zero.")
    return force_n / area_m2


def main() -> None:
    force_n = 120_000.0
    area_m2 = 0.0008
    stress_pa = calculate_stress_pa(force_n, area_m2)
    report = {
        "calculation": "axial_stress",
        "inputs": {"force_n": force_n, "area_m2": area_m2},
        "formula": "stress_pa = force_n / area_m2",
        "assumptions": ["uniform axial force", "positive area"],
        "result": {"stress_mpa": round(stress_pa / 1_000_000, 3)},
        "created_at": datetime.now(timezone.utc).isoformat(),
        "warning": "Educational result; requires qualified engineering review.",
    }
    output_path = Path(__file__).parent / "calculation_report.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
