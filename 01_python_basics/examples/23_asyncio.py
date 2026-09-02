"""Use asyncio with simulated inspection tasks only."""

import asyncio
import math


def pressure_pa(force_n: float, area_m2: float) -> float:
    """Return a deterministic pressure after validating inputs."""
    if not math.isfinite(force_n) or not math.isfinite(area_m2):
        raise ValueError("force and area must be finite numbers")
    if force_n < 0:
        raise ValueError("force must be zero or greater")
    if area_m2 <= 0:
        raise ValueError("area must be greater than zero")
    return force_n / area_m2


async def inspect_part(part_id: str, delay_s: float, force_n: float) -> str:
    """Simulate waiting for an inspection result; no device is contacted."""
    await asyncio.sleep(delay_s)
    pressure = pressure_pa(force_n, 0.006)
    return f"{part_id}: {pressure:.0f} Pa"


async def main() -> None:
    reports = await asyncio.gather(
        inspect_part("P-01", 0.03, 12_000),
        inspect_part("P-02", 0.01, 9_000),
        inspect_part("P-03", 0.02, 15_000),
    )
    for report in reports:
        print(report)


if __name__ == "__main__":
    asyncio.run(main())
