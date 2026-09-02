# Module 2 examples

Run these examples from the MSYS2 UCRT64 terminal after activating the project `.venv`:

```bash
cd 02_engineering_code/examples
python examples.py
python -m pytest
```

`examples.py` is an end-to-end walkthrough: it calls validated, typed functions in `calculations.py`; reads CSV rows using named headers; converts text values to `float`; converts load from kN to N; produces stress in MPa; exports results as JSON; and catches invalid zero-area input clearly.

`test_calculations.py` tests normal rectangle and stress calculations plus the invalid zero-area boundary. Add a test whenever a calculation rule changes.

Do not treat sample results as design approval. Check source data, units, formula assumptions, and applicable engineering requirements.
