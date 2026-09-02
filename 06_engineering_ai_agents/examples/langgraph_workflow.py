"""A deterministic LangGraph workflow with explicit state and routing."""
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph

from engineering_tools import calculate_stress


class EngineeringState(TypedDict, total=False):
    force_n: float
    area_m2: float
    status: str
    error: str
    result: dict[str, float | str]
    report: str


def validate_inputs(state: EngineeringState) -> EngineeringState:
    if "force_n" not in state or "area_m2" not in state:
        return {"status": "needs_input", "error": "force_n and area_m2 are required"}
    if state["force_n"] < 0 or state["area_m2"] <= 0:
        return {"status": "invalid_input", "error": "Check force and area ranges"}
    return {"status": "ready"}


def route_after_validation(state: EngineeringState) -> Literal["calculate", "stop"]:
    return "calculate" if state["status"] == "ready" else "stop"


def calculate(state: EngineeringState) -> EngineeringState:
    return {"status": "calculated", "result": calculate_stress(state["force_n"], state["area_m2"])}


def create_report(state: EngineeringState) -> EngineeringState:
    result = state["result"]
    return {"status": "complete", "report": f"Stress = {result['value']} {result['unit']}"}


def build_workflow():
    builder = StateGraph(EngineeringState)
    builder.add_node("validate", validate_inputs)
    builder.add_node("calculate", calculate)
    builder.add_node("report", create_report)
    builder.add_node("stop", lambda state: {})
    builder.add_edge(START, "validate")
    builder.add_conditional_edges("validate", route_after_validation)
    builder.add_edge("calculate", "report")
    builder.add_edge("report", END)
    builder.add_edge("stop", END)
    return builder.compile()


if __name__ == "__main__":
    workflow = build_workflow()
    final_state = workflow.invoke({"force_n": 120_000.0, "area_m2": 0.0008})
    print(final_state)
