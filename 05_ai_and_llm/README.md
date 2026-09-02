# Module 5: OpenAI API and LLM Fundamentals

This module uses the official OpenAI Python SDK and the Responses API.

## Setup in MSYS2 UCRT64

Activate the course virtual environment and install the dependencies:

```bash
source .venv/Scripts/activate
python -m pip install openai pydantic
```

Create an API key in the OpenAI API dashboard, then expose it to the current terminal session:

```bash
export OPENAI_API_KEY="your_key"
export OPENAI_MODEL="gpt-5.6"
```

`OPENAI_MODEL` is optional. The examples default to the model used by the official quickstart when these lessons were written. Your OpenAI project must have access to the selected model.

Never store a real API key in this repository.

## Examples

- `01_first_response.py` — a minimal Responses API request.
- `02_explain_verified_calculation.py` — Python calculates; OpenAI explains supplied facts.
- `03_structured_measurement.py` — typed Structured Outputs with Pydantic followed by application validation.
- `04_error_handling.py` — safe handling of authentication, rate-limit, connection, and API-status errors.
- `safe_llm_boundary.py` — offline JSON-validation example that does not call an API.

## Official documentation

- [OpenAI Developer quickstart](https://developers.openai.com/api/docs/quickstart)
- [OpenAI SDKs](https://developers.openai.com/api/docs/libraries)
- [Text generation](https://developers.openai.com/api/docs/guides/text)
- [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [API error codes](https://developers.openai.com/api/docs/guides/error-codes)

Generated output is not verified engineering evidence. Numerical calculations must use validated and tested Python functions, and consequential decisions require qualified review.
