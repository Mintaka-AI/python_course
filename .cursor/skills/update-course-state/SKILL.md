---
name: update-course-state
description: Updates student progress in state.json after theory, examples, or code review. Use after checking answers, completing a task, or transitioning between modules.
---

# Updating Progress in state.json

## File

`state.json` in the project root.

## Operations

### Session Start

```json
"course": {
  "last_session": "2026-09-02T15:30:00+04:00"
},
"modules": {
  "{id}": {
    "status": "in_progress"
  }
}
```

### Theory Mastered

```json
"theory": {
  "mastered": true,
  "score": 80,
  "attempts": 1,
  "last_checked": "2026-09-02T15:30:00+04:00",
  "notes": "brief comment"
}
```

### Example Completed

```json
"examples": {
  "completed": ["task_01"],
  "mastered": true,
  "attempts": 1,
  "last_checked": "2026-09-02T15:30:00+04:00",
  "notes": ""
}
```

### Code Accepted

```json
"code": {
  "completed": ["unit_converter"],
  "mastered": true,
  "attempts": 2,
  "last_checked": "2026-09-02T15:30:00+04:00",
  "notes": "passed on second attempt"
}
```

### Module Completed

When `theory.mastered`, `examples.mastered`, and `code.mastered` are all `true`:

```json
"status": "completed"
```

Update `course.current_module` to the next module ID.

## Rules

1. Preserve the structure — do not remove fields or modules.
2. Increment `attempts` on each review.
3. Write specific `notes`.
4. Dates must be ISO 8601.
5. Do not unlock the next module until the current one is `completed`.
6. Keep valid JSON syntax.

## Module Statuses

| Status | Condition |
|--------|-----------|
| `not_started` | Student has not started |
| `in_progress` | Learning in progress |
| `completed` | All three `mastered: true` |
