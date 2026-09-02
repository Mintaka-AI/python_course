"""Send a first text request with the OpenAI Responses API.

MSYS2 UCRT64 setup:
    python -m pip install openai
    export OPENAI_API_KEY="your_key"
    export OPENAI_MODEL="gpt-5.6"  # optional
    python 01_first_response.py
"""

import os

from openai import OpenAI


def main() -> None:
    """Request a short explanation and print the generated text."""
    client = OpenAI()
    model_name = os.getenv("OPENAI_MODEL", "gpt-5.6")

    response = client.responses.create(
        model=model_name,
        input="Explain in two sentences why engineering calculations need units.",
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
