"""Run with: python -m pytest test_engineering_agent.py"""
from engineering_agent import run_tool


def test_success() -> None:
    response = run_tool("calculate_stress", {"force_n": 120_000, "area_m2": 0.0008})
    assert response["status"] == "ok"
    assert response["result"]["value"] == 150.0


def test_missing_input() -> None:
    assert run_tool("calculate_stress", {"force_n": 120_000})["status"] == "needs_input"


def test_unknown_tool_is_refused() -> None:
    assert run_tool("delete_files", {})["status"] == "refused"
