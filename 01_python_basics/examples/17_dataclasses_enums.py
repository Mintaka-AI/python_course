"""Lesson 17: dataclasses, enums, and useful special methods."""

from dataclasses import dataclass
from enum import Enum
import math


class TestStatus(Enum):
    PLANNED = "planned"
    PASSED = "passed"
    FAILED = "failed"


@dataclass
class BeamTest:
    test_id: str
    load_kn: float
    status: TestStatus = TestStatus.PLANNED

    def __post_init__(self) -> None:
        if not math.isfinite(self.load_kn) or self.load_kn <= 0:
            raise ValueError("Test load must be a finite number greater than zero.")

    def __str__(self) -> str:
        return f"{self.test_id}: {self.load_kn:.1f} kN ({self.status.value})"

    def safety_factor(self, rated_load_kn: float) -> float:
        if not math.isfinite(rated_load_kn) or rated_load_kn <= 0:
            raise ValueError("Rated load must be a finite number greater than zero.")
        return rated_load_kn / self.load_kn


test = BeamTest("B-17", 24.0, TestStatus.PASSED)
same_test = BeamTest("B-17", 24.0, TestStatus.PASSED)

print(test)
print(f"Debug form: {test!r}")
print(f"Tests equal: {test == same_test}")
print(f"Safety factor: {test.safety_factor(60.0):.2f}")
