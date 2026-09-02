"""Lesson 26: read a text file using Path and with."""

from pathlib import Path


example_folder = Path(__file__).parent
note_path = example_folder / "module_1_note.txt"

with note_path.open(encoding="utf-8") as note_file:
    note_text = note_file.read()

print(f"Read from: {note_path.name}")
print(note_text)
