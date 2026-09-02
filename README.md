<p align="center">
  <img src="assets/mintaka-logo.png" alt="Mintaka-AI logo" width="160">
</p>

# Python for Engineering AI Agents

A beginner-friendly, project-based Python course for engineering and mathematics.
It starts with environment setup and Python fundamentals, then progresses through
reliable engineering calculations, data analysis, the OpenAI API, tool-calling
agents, LangChain, LangGraph, and Model Context Protocol (MCP).

The course is written in English and designed for **Windows with MSYS2 UCRT64**.
Theory is provided as local HTML lessons, while every module includes runnable
Python examples and practical exercises.

Developed by [Mintaka-AI](https://mintaka-ai.com/) — AI-powered engineering.

## What You Will Learn

By completing the course, you will learn how to:

- write clear Python programs from the beginning;
- organize code into functions, modules, and small projects;
- validate input and handle errors safely;
- test engineering formulas with `pytest`;
- work with NumPy, SymPy, pandas, and Matplotlib;
- handle physical units and build verifiable engineering calculators;
- use the official OpenAI Python SDK and Responses API;
- create structured outputs and function-calling tools;
- build agents with LangChain and workflows with LangGraph;
- create tools, resources, and prompts with an MCP server;
- keep AI-generated explanations separate from verified calculations.

## Course Modules

| Module | Topic | Main outcome |
|---|---|---|
| 0 | Environment Setup | Configure MSYS2 UCRT64, Python, Git, VS Code, and a virtual environment |
| 1 | Python Basics | Learn Python syntax, types, conditions, loops, collections, and functions |
| 2 | Quality Engineering Code | Use files, exceptions, modules, type hints, project structure, and tests |
| 3 | Mathematics and Data | Work with NumPy, SymPy, pandas, and Matplotlib |
| 4 | Engineering Calculations | Build validated calculation tools with explicit units and assumptions |
| 5 | AI and LLM Fundamentals | Use the OpenAI SDK, Responses API, and Structured Outputs safely |
| 6 | Engineering AI Agents | Build tool-calling agents, LangChain agents, LangGraph workflows, and MCP servers |

The detailed curriculum is available in [Docs/plan.md](Docs/plan.md).

## Repository Structure

```text
python_cource1/
├── 00_environment/
├── 01_python_basics/
├── 02_engineering_code/
├── 03_math_and_data/
├── 04_engineering_calculations/
├── 05_ai_and_llm/
├── 06_engineering_ai_agents/
│   ├── theory/                 # HTML lessons
│   └── examples/               # Python programs and exercises
├── assets/                     # Shared CSS, JavaScript, and images
├── Docs/                       # Course plan and documentation
├── AGENTS.md                   # Instructions for an AI course instructor
├── help.html                   # How to study with Codex or Cline
├── index.html                  # Main course menu
├── summary.html                # Progress dashboard
└── state.json                  # Student progress record
```

## Requirements

- Windows 10 or Windows 11
- [MSYS2](https://www.msys2.org/)
- MSYS2 **UCRT64** terminal
- Python 3.14 or the current UCRT64 Python package
- Git
- VS Code or another compatible editor

All commands in this course are intended for the **MSYS2 UCRT64 terminal**.
Do not run the setup commands in PowerShell, Command Prompt, MSYS, or MINGW64.

## Quick Start

### 1. Install the UCRT64 tools

Open the **MSYS2 UCRT64** terminal and update the system:

```bash
pacman -Syu
```

If MSYS2 asks you to close the terminal, reopen **MSYS2 UCRT64** and run the
command again. Then install Python and Git:

```bash
pacman -S mingw-w64-ucrt-x86_64-python mingw-w64-ucrt-x86_64-python-pip mingw-w64-ucrt-x86_64-python-virtualenv git
```

### 2. Open the cloned project

After cloning or downloading the repository, move to its root. For the default
course location used in the lessons:

```bash
cd /c/msys64/home/user1/projects/cources/python_cource1
```

If you cloned it elsewhere, replace this path with your actual repository path.

### 3. Create a virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate
python --version
python -m pip --version
which python
```

`which python` should point to `.venv` or the UCRT64 Python installation.

### 4. Install course libraries

Install the scientific and testing packages:

```bash
python -m pip install pytest numpy scipy sympy pandas openpyxl matplotlib pint
```

For Modules 5 and 6, install the AI and agent packages:

```bash
python -m pip install openai pydantic langchain langchain-openai langgraph "mcp[cli]"
```

## Open the Course Website

Start a local web server from the project root:

```bash
python -m http.server 8000
```

Open these pages in a browser:

- [Course menu](http://localhost:8000/index.html)
- [Progress dashboard](http://localhost:8000/summary.html)
- [AI instructor help](http://localhost:8000/help.html)

The web server is recommended because the progress dashboard loads
`state.json` with JavaScript. Some browsers block that request when an HTML file
is opened directly through `file://`. Stop the server with `Ctrl+C`.

## Run an Example

Activate `.venv`, move to an example directory, and run the file with Python:

```bash
cd 01_python_basics/examples
python 02_variables_and_types.py
```

Run tests with:

```bash
python -m pytest test_file_name.py -q
```

Read the README inside each module for module-specific dependencies and commands.

## Use Codex or Cline as the Instructor

Open the complete `python_cource1` directory as your VS Code workspace. The AI
agent needs access to `AGENTS.md`, `state.json`, the course plan, theory files,
and examples.

Start with this prompt:

```text
Act as my instructor for this Python course. Read AGENTS.md, state.json,
Docs/plan.md, and Docs/state-schema.md first. Identify my current module,
open the next HTML theory lesson in the internal browser, explain it in simple
English, help me run the example in MSYS2 UCRT64, ask 2–4 questions, give me a
practical task, and update state.json only after reviewing my actual work.
Do not move to the next module until theory, examples, and code are mastered.
```

The full instructor workflow, ready-to-copy prompts, browser instructions, and
progress rules are in [help.html](help.html).

## Student Progress

Progress is stored in [state.json](state.json). Each module tracks three areas:

- `theory` — mastered after at least 75% correct answers;
- `examples` — mastered after the student explains or reproduces the example;
- `code` — mastered after a working practical solution is reviewed.

The AI instructor must update progress only after an actual review. Opening a
lesson or running supplied code does not automatically prove mastery. A module
is completed only when all three areas are mastered.

See [Docs/state-schema.md](Docs/state-schema.md) for the complete data format.

## OpenAI API Setup

Modules 5 and 6 contain optional examples that call the OpenAI API. Set the key
only in the current MSYS2 UCRT64 terminal session:

```bash
export OPENAI_API_KEY="your_api_key"
export OPENAI_MODEL="gpt-5.6"
```

`OPENAI_MODEL` is optional and can be changed to a model available to your
OpenAI project.

Never commit API keys, tokens, passwords, `.env` files containing secrets, or
private engineering data to the repository.

## Engineering and AI Safety

This repository is educational. Its examples do not replace professional
engineering judgment, independent verification, applicable standards, or a
qualified review.

- Numerical results must come from validated and tested Python functions.
- Model-generated text is not verified engineering evidence.
- Units, formulas, assumptions, and limitations must remain visible.
- Agents must use narrow allowlisted tools and bounded workflows.
- Do not let course agents control equipment or make autonomous safety-critical decisions.

## Documentation and Sources

Python lessons use the official Python 3.14 documentation as the primary
technical reference. Third-party lessons link to the official documentation for
OpenAI, LangChain, LangGraph, MCP, and the scientific Python libraries.

See [sources.html](sources.html) for the source and attribution list.

## Copyright

Copyright © Mintaka-AI LLC. All rights reserved.

No open-source license file is currently included in this repository. Public
availability on GitHub does not by itself grant permission to copy, modify, or
redistribute the course materials.
