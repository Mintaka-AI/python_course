# Module 6: Engineering AI Agents

This module teaches agent loops, OpenAI Responses API function calling, LangChain agents,
LangGraph workflows, MCP servers, verifiable computations, and action logs.

## Structure

- `theory/` — HTML theory lessons
- `examples/` — code samples and practical exercises

## Install the optional libraries

In the MSYS2 UCRT64 terminal, activate the course virtual environment and run:

```bash
python -m pip install openai langchain langchain-openai langgraph "mcp[cli]"
```

Set `OPENAI_API_KEY` before running examples that call OpenAI. You may override the
default model with `OPENAI_MODEL`. The offline example and its tests need no API key.

## Examples

- `engineering_agent.py` — offline allowlist, validation, and action log
- `openai_tool_agent.py` — manual Responses API function-calling loop
- `langchain_agent.py` — high-level LangChain agent
- `langgraph_workflow.py` — explicit state, nodes, edges, and routing
- `mcp_engineering_server.py` — MCP tool, resource, and prompt
- `test_engineering_agent.py` — deterministic tests
