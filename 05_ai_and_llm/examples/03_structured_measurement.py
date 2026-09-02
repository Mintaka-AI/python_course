"""Extract typed measurement data with OpenAI Structured Outputs.

Requires:
    python -m pip install openai pydantic
"""

import os

from openai import OpenAI
from pydantic import BaseModel


class MeasurementExtraction(BaseModel):
    """Schema for one explicitly stated engineering measurement."""

    quantity: str
    value: float
    unit: str
    missing_information: list[str]


ALLOWED_QUANTITIES = {"force"}
ALLOWED_UNITS = {"N", "kN"}


def validate_measurement(measurement: MeasurementExtraction) -> None:
    """Apply application rules after model-output schema validation."""
    if measurement.quantity not in ALLOWED_QUANTITIES:
        raise ValueError(f"Unsupported quantity: {measurement.quantity}")
    if measurement.unit not in ALLOWED_UNITS:
        raise ValueError(f"Unsupported unit: {measurement.unit}")
    if measurement.value < 0:
        raise ValueError("Force must not be negative.")


def main() -> None:
    """Extract, validate, and display a measurement without calculating stress."""
    client = OpenAI()
    response = client.responses.parse(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6"),
        input=[
            {
                "role": "system",
                "content": (
                    "Extract only explicitly stated measurement data. "
                    "Report information required for axial stress but missing from the text."
                ),
            },
            {"role": "user", "content": "The applied force is 12.5 kN."},
        ],
        text_format=MeasurementExtraction,
    )

    measurement = response.output_parsed
    if measurement is None:
        raise RuntimeError("The response did not contain parsed measurement data.")

    validate_measurement(measurement)
    print(measurement.model_dump_json(indent=2))

    if measurement.missing_information:
        print("Calculation stopped: required information is missing.")


if __name__ == "__main__":
    main()
