"""Module 1 examples index.

Run an individual file from the MSYS2 UCRT64 terminal, for example:
    python 06_for_loops.py
"""

LESSON_EXAMPLES = (
    "01_syntax_and_output.py",
    "02_variables_and_types.py",
    "03_operators.py",
    "04_input.py",
    "05_conditions.py",
    "06_for_loops.py",
    "07_while_loops.py",
    "08_collections.py",
    "09_functions.py",
    "10_strings_and_fstrings.py",
    "11_running_and_debugging.py",
    "12_comprehensions_preview.py",
    "25_imports_and_modules.py",
    "26_paths_and_files.py",
    "27_try_except_basics.py",
)

PRACTICE_EXAMPLES = (
    "week2_geometry_and_mass.py",
    "week2_motion.py",
    "week3_function_table.py",
    "week4_materials_db.py",
    "week4_shape_areas.py",
    "beam_check.py",
)

ADVANCED_EXAMPLES = (
    "13_iterators_generators.py",
    "14_lambda_higher_order.py",
    "15_args_closures_decorators.py",
    "16_oop_basics.py",
    "17_dataclasses_enums.py",
    "18_advanced_typing.py",
    "19_exceptions_context_managers.py",
    "20_logging_configuration.py",
    "21_packaging_cli.py",
    "22_concurrency_concepts.py",
    "23_asyncio.py",
    "24_engineering_agent_patterns.py",
)

print("Module 1 lesson examples:")
for filename in LESSON_EXAMPLES:
    print(f"  python {filename}")

print("\nModule 1 practice examples:")
for filename in PRACTICE_EXAMPLES:
    print(f"  python {filename}")

print("\nModule 1 Advanced Python examples:")
for filename in ADVANCED_EXAMPLES:
    print(f"  python {filename}")
