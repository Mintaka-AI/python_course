# Course Plan: Python for Engineering AI Agents

## Who the Course Is For

The course is designed for beginners who are just starting to learn Python. No prior programming experience or knowledge of artificial intelligence is required.

## Main Goal

Learn to build simple AI agents that help solve engineering and mathematical problems: performing calculations, working with formulas and units of measurement, plotting results, analyzing data, and preparing reports.

## Learning Outcomes

After completing the course, the student will be able to:

- write clear Python programs;
- automate engineering calculations;
- read and process data from CSV and Excel files;
- plot results;
- use mathematical libraries;
- connect a language model to a Python program;
- build an AI agent with a set of tools for engineering tasks;
- verify and document calculation results.

## Format

- Duration: 16 weeks.
- Workload: 6–8 hours per week.
- Each week: short theory, explained examples, practical exercises, and a mini-project.
- Core principle: first solve the task with ordinary code, then give an AI agent safe tools to solve it.

## Required Lesson Materials Standard

All course materials must be written in English and use a focused, beginner-friendly format similar to the structure of W3Schools lessons. Module 1 is the reference implementation for this standard.

### Technical Sources

- Python language and standard-library material uses the official Python 3.14 documentation as the primary technical reference.
- Every Python lesson links to the relevant Python 3.14 documentation for deeper study.
- Third-party topics use the official documentation for that library: NumPy, SymPy, pandas, Matplotlib, Pint, pytest, or the selected LLM SDK.
- Course explanations and engineering examples are original educational material; source text is not copied into lessons.
- See `sources.html` for attribution and `Docs/lesson-standard.md` for the full lesson checklist.

### Theory Materials

- Store theory in separate HTML pages in each module's `theory/` folder.
- Cover one Python concept or closely related topic per page.
- Add a module `index.html` page with links to all lessons in learning order.
- Every lesson page must include:
  1. short, plain-language explanation;
  2. syntax or a minimal code pattern;
  3. a runnable code example;
  4. an explanation of the expected result;
  5. an engineering or mathematics example where appropriate;
  6. a "Try it yourself" exercise;
  7. Previous, Module index, and Next navigation links where applicable.
- Use the shared resources from `assets/css/course.css` and `assets/js/course.js`.
- Use `.note`, `.warning`, and `.exercise` blocks to highlight important information.
- Explain new terms before using them. Do not assume previous programming experience.

### Example Materials

- Store runnable Python files in each module's `examples/` folder.
- Keep examples aligned with the theory pages in the same module.
- Use clear section comments and meaningful engineering variable names with units, such as `force_n` and `area_m2`.
- Each example file must run successfully in Windows + MSYS2 UCRT64.
- Avoid interactive input in examples that must run automatically; place optional interactive code in a clearly marked section.

## Fixed Working Environment

The entire course uses **Windows + MSYS2 UCRT64** only. All commands from the lessons are run in the **MSYS2 UCRT64** shortcut — not in PowerShell, Command Prompt, MSYS, or MINGW64.

- Python is installed from the UCRT64 repository via `pacman`.
- Python packages are installed with `python -m pip` to ensure the UCRT64 Python is used.
- A virtual environment `.venv` is created in each project.
- VS Code or Cursor opens the built-in **MSYS2 UCRT64** terminal and uses the `.venv` interpreter.

---

## Module 0. Preparing the Working Environment

**Week 1**

Topics:

- What Python is and where it is used in engineering.
- Installing MSYS2 and launching the **MSYS2 UCRT64** shortcut.
- Updating packages: `pacman -Syu`. If required, close the terminal, reopen **MSYS2 UCRT64**, and repeat the command.
- Installing Python and basic UCRT64 tools: `pacman -S mingw-w64-ucrt-x86_64-python mingw-w64-ucrt-x86_64-python-pip mingw-w64-ucrt-x86_64-python-virtualenv git`.
- Configuring VS Code or Cursor: default terminal — **MSYS2 UCRT64**.
- Running programs and working with paths in the UCRT64 terminal.
- Files, folders, and virtual environments.
- Installing libraries with `python -m pip`.
- Git: only the basic commands for saving projects.

Practice:

- Create a first program: converting temperature, length, and mass between units.
- Create an environment: `python -m venv .venv`, then activate it: `source .venv/Scripts/activate`.
- Verify that `python --version`, `python -m pip --version`, and `which python` point to UCRT64 or `.venv`.

---

## Module 1. Python Basics

**Weeks 2–4**

### Complete Python Language Scope: Basic and Advanced

This section defines the complete Python language path used by the course. Module 1 teaches the foundation first. Topics marked as advanced are introduced later, when students have enough practice to use them safely in engineering programs.

#### Basic Python: required foundation

1. **Syntax and program execution**
   - Statements, expressions, indentation, comments, and code blocks.
   - Running a `.py` file from the MSYS2 UCRT64 terminal.
   - Reading error messages and tracebacks at a beginner level.

2. **Values, variables, and built-in types**
   - Assignment, reassignment, naming rules, `snake_case`, constants by convention, and variables with units.
   - Numbers: `int`, `float`, arithmetic, rounding, and numerical precision basics.
   - Text: `str`, quotes, f-strings, indexing, slicing, and common string methods.
   - Logical values: `bool`, `True`, `False`, truthiness, and `None`.
   - Casting and conversion: `int()`, `float()`, `str()`, `bool()`, and `type()`.

3. **Operators and expressions**
   - Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, and `**`.
   - Comparisons: `==`, `!=`, `<`, `>`, `<=`, and `>=`.
   - Logical operators: `and`, `or`, and `not`.
   - Assignment operators and operator precedence.

4. **Control flow**
   - `if`, `elif`, and `else`.
   - `for` loops, `while` loops, `range()`, `break`, `continue`, and loop `else`.
   - Nested conditions and loops.

5. **Data structures**
   - Lists: indexing, slicing, adding/removing items, sorting, copying, and list methods.
   - Tuples and unpacking.
   - Sets: unique values and set operations.
   - Dictionaries: keys, values, `get()`, `items()`, updating, and looping through records.
   - Built-in functions: `len()`, `min()`, `max()`, `sum()`, `sorted()`, `enumerate()`, `zip()`, `any()`, and `all()`.

6. **Functions**
   - Defining and calling functions with `def`.
   - Parameters, arguments, return values, default arguments, and keyword arguments.
   - Local and global scope.
   - Docstrings and clear function design for engineering calculations.

7. **Files, errors, and modules**
   - Imports, modules, packages, and the standard library.
   - Text, CSV, and JSON files; paths and the `with` statement.
   - Exceptions: `try`, `except`, `else`, `finally`, and `raise`.
   - Input validation and meaningful error messages.

8. **Quality and verification**
   - Type hints, formatting, and readable project structure.
   - Assertions and automated tests with `pytest`.
   - Debugging with print statements and an IDE debugger.

#### Optional Advanced Python Track: post-foundation

1. **Comprehensions and iterable tools**
   - List, dictionary, and set comprehensions.
   - Iterators, generators, `yield`, generator expressions, and lazy processing of large datasets.

2. **Functional and reusable code**
   - Lambda expressions, `map()`, `filter()`, `sorted(key=...)`, and higher-order functions.
   - Closures and decorators.
   - `*args` and `**kwargs`.

3. **Object-oriented programming**
   - Classes, objects, attributes, methods, inheritance, composition, and properties.
   - Dataclasses, enums, abstract base classes, and protocols.
   - Special methods such as `__init__`, `__str__`, and `__repr__`.

4. **Resource and error management**
   - Custom exception classes.
   - Context managers and `with`.
   - Logging and configuration through environment variables.

5. **Modern Python development**
   - Advanced type hints: `list[str]`, `dict[str, float]`, `Optional`, `Union`, `Literal`, `TypedDict`, `Protocol`, and generics.
   - Virtual environments, dependency management, package layout, and command-line programs.

6. **Concurrency and asynchronous code**
   - The difference between synchronous, threaded, process-based, and asynchronous programs.
   - `async`, `await`, `asyncio`, and safe use cases for API-based AI agents.

7. **Engineering and AI-agent application**
   - Numerical and symbolic libraries, data analysis, plotting, API clients, tool functions, structured JSON, and testing.
   - Safe separation of language-model text generation from deterministic engineering calculations.

> The optional Advanced Python Track lives inside Module 1 as a post-foundation learning path. Students complete the required foundation first, then may study these lessons before applying the ideas in later modules and project work. The track is not required for completing the beginner foundation.

### Week 2. Variables and Calculations

Topics:

- Variables and data types: numbers, strings, logical values.
- Arithmetic operations.
- Input and output: `input()` and `print()`.
- Comments and meaningful variable names.

Practice:

- A calculator for the area, volume, and mass of a part.
- Calculating speed, time, and traveled distance.

### Week 3. Conditions and Loops

Topics:

- Conditions: `if`, `elif`, `else`.
- Comparisons and logical operators.
- `for` and `while` loops.
- Typical beginner mistakes.

Practice:

- Checking an allowable load on a beam against a given limit.
- A table of function values on a chosen interval.

### Week 4. Collections and Functions

Topics:

- Lists, dictionaries, tuples, and sets.
- Functions, parameters, and return values.
- Variable scope.
- Splitting a large task into small functions.

Practice:

- A program for storing material properties.
- A set of functions for calculating the area of standard shapes.

---

## Module 2. Quality Engineering Code

**Weeks 5–6**

### Week 5. Files and Error Handling

Topics:

- Reading and writing text files, CSV, and JSON.
- The `with` statement.
- Error handling: `try`, `except`, `finally`.
- Input validation.

Practice:

- Loading measurements from a CSV file.
- A program that reports a clear error message for invalid data.

### Week 6. Project Structure and Tests

Topics:

- Modules and imports.
- Structure of a small Python project.
- Type hints.
- Testing basics with `pytest`.
- Why engineering calculations must be tested.

Practice:

- Package the calculator as a project.
- Write tests for the volume and density formulas.

---

## Module 3. Math and Data Analysis in Python

**Weeks 7–10**

### Week 7. NumPy

Topics:

- NumPy arrays.
- Vectorized computations.
- Working with ranges and matrices.
- Numerical errors and rounding.

Practice:

- Calculating a series of stress and strain values.
- Simple matrix operations.

### Week 8. SymPy and Formulas

Topics:

- Symbolic expressions.
- Solving equations.
- Derivatives and integrals.
- Substituting numerical values into formulas.

Practice:

- Solving a quadratic equation.
- Deriving and calculating a formula for an engineering problem.

### Week 9. Pandas and Tabular Data

Topics:

- `DataFrame` tables.
- Loading CSV and Excel files.
- Filtering, grouping, and cleaning data.
- Basic statistics of measurements.

Practice:

- Analyzing a set of sensor readings.
- Finding gaps and outliers in measurements.

### Week 10. Plotting

Topics:

- Plotting with `matplotlib`.
- Axis labels, units, legends, and grid.
- Several plots in one figure.
- Saving plots to files.

Practice:

- A load–strain plot.
- An automatic report with a table and a chart.

---

## Module 4. Engineering Calculations as Tools

**Weeks 11–12**

### Week 11. Reliable Calculation Functions

Topics:

- Unit conversion with `pint`.
- Parameters, assumptions, and limits of formulas.
- Dimension checking.
- Documenting functions.

Practice:

- A calculator for mechanical properties: force, pressure, stress, torque.
- Checking compatibility of units.

### Week 12. Mini-Project: Engineering Calculator

Task:

- Build a console or simple web application for engineering calculations.
- Add data input, error checking, results in the required units, plots, and report export.

Example topics:

- beam calculation;
- pipeline calculation;
- thermal calculation;
- electrical circuit analysis;
- processing experimental measurements.

---

## Module 5. AI, OpenAI API, and LLM Fundamentals

**Weeks 13–14**

### Week 13. How Language Models Work

Topics:

- What AI can and cannot do.
- What an LLM is; a model's request and response.
- The difference between ChatGPT as an application and the OpenAI API as an interface for programs.
- The role of system instructions and context.
- Why a model's response must never be treated as an engineering calculation result without verification.
- Data confidentiality and safe use of API keys.

Practice:

- Writing precise prompts to explain formulas.
- Comparing a model's answer with the result of a Python computation.

### Week 14. OpenAI API and the Official Python SDK

Topics:

- Installing the official `openai` package with `python -m pip`.
- API: request, response, access key, and the `OPENAI_API_KEY` environment variable.
- Responses API: `OpenAI()`, `client.responses.create()`, and `response.output_text`.
- Separating `instructions` and `input`.
- Structured Outputs via `client.responses.parse()` and Pydantic.
- Validating a structured response before an engineering calculation.
- Handling authentication, connection, rate limit, and HTTP status errors.

Practice:

- A helper program on the OpenAI Responses API that explains an already verified calculation.
- Extracting a measurement through Structured Outputs without substituting missing data.
- Preventing the model from inventing numerical results: computations are performed only by a verified Python function.

---

## Module 6. AI Agents for Engineering

**Weeks 15–16**

### Week 15. Agent and Its Tools

Topics:

- What an AI agent is.
- The difference between a chatbot and an agent.
- Agent tools: calculator, Python functions, documentation search, file handling.
- The working cycle: receive a task → choose a tool → perform the calculation → verify the result → explain the answer.
- Access restrictions and action logging.
- OpenAI Responses API: JSON Schema function descriptions, `function_call`, executing an allowed Python function, and `function_call_output`.
- A bounded agent loop: maximum number of steps, error handling, argument validation, and rejecting unknown tools.
- LangChain: `create_agent()`, typed Python tools, messages, and agent invocation.
- LangGraph: state, nodes, edges, conditional transitions, explicit validation before calculation and reporting.
- When to use the direct OpenAI SDK, LangChain, or LangGraph.

Practice:

- Build an agent that selects the right function from a library of engineering calculations.
- Add a log: input data, chosen formula, units, and result.
- Implement the same safe calculation through the OpenAI SDK and through LangChain.
- Build a deterministic LangGraph process: validate → calculate → report or refuse.

### MCP: Portable Tools and Context

Topics:

- MCP host, client, and server.
- MCP tools, resources, and prompts; who chooses each capability type.
- The official Python SDK: `MCPServer`, decorators, type annotations, and docstrings as schema.
- Local `stdio` transport and remote `streamable-http`.
- Connecting a remote MCP server to the OpenAI Responses API.
- Tool allow-lists, action confirmation, authentication, and data protection.

Practice:

- Create a local MCP server with an engineering tool, a resource with constraints, and a result-explanation prompt template.
- Test the server with MCP Inspector.
- Design a confirmation policy for read-only and data-modifying tools.

### Week 16. Final Project

Build an AI agent for one engineering domain.

Required capabilities:

- accept a task written in natural language;
- ask clarifying questions when data is missing;
- extract numbers and units of measurement;
- use only verified Python functions for computations;
- show the formula, assumptions, units, and calculation steps;
- plot results when necessary;
- save the result as a report;
- state clearly when a task is beyond the agent's capabilities.

Example final projects:

- an agent for strength calculations of simple elements;
- an agent for electrical engineering calculations;
- an agent for thermal calculations;
- an agent for analyzing laboratory measurements;
- an agent for selecting materials by given parameters.

---

## Safety Rules for Engineering AI

- An AI agent does not replace an engineer and does not make decisions in tasks involving risk to people, equipment, or infrastructure.
- All formulas, input data, units of measurement, and results must be verifiable.
- Safety-critical calculations must be checked by a qualified specialist and against regulatory documentation.
- The agent must clearly show its assumptions and be able to refuse tasks with incomplete or unreliable data.

## Recommended Libraries

- `pytest` — testing calculations.
- `numpy` — numerical computing.
- `sympy` — formulas and symbolic math.
- `pandas` — tables and data.
- `matplotlib` — plots.
- `pint` — units of measurement.
- `openpyxl` — working with Excel.
- `openai` — official Python SDK and Responses API.
- `langchain` and `langchain-openai` — high-level agents and OpenAI integration.
- `langgraph` — explicit states and controlled agent workflows.
- `mcp` — official Python SDK for MCP clients and servers.
- SDK of the chosen LLM provider — connecting a language model.

## Completion Criteria

The student has completed the course if the final project:

1. runs from a clear set of instructions;
2. contains tests for key formulas;
3. validates invalid input and units of measurement;
4. uses AI only for dialogue, request analysis, and explanation;
5. performs numerical calculations with verified Python code;
6. produces a clear result with the formula, units, and limitations.