"""Handle common OpenAI SDK failures without exposing secrets."""

import os

import openai
from openai import OpenAI


def main() -> None:
    """Make a small request and report safe error categories."""
    client = OpenAI()
    model_name = os.getenv("OPENAI_MODEL", "gpt-5.6")

    try:
        response = client.responses.create(
            model=model_name,
            input="Reply with exactly: API connection succeeded.",
        )
    except openai.AuthenticationError:
        print("Authentication failed. Check the configured API key.")
    except openai.RateLimitError:
        print("The request was rate limited. Retry later according to policy.")
    except openai.APIConnectionError:
        print("Could not connect to the OpenAI API.")
    except openai.APIStatusError as error:
        print(f"OpenAI API returned HTTP status {error.status_code}.")
    else:
        print(response.output_text)


if __name__ == "__main__":
    main()
