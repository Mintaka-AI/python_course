# Student Progress Data Schema

The instructor updates `state.json` in the project root after each knowledge check.
The dashboard in `index.html` reads the same file to display progress.

## Root Object `course`

| Field | Type | Description |
|-------|------|-------------|
| `student` | string | Student name |
| `current_module` | string | Active module ID (`00_environment` … `06_engineering_ai_agents`) |
| `started_at` | string \| null | Course start date (ISO 8601) |
| `last_session` | string \| null | Last session date (ISO 8601) |

## Module Object

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Module title |
| `status` | enum | `not_started` → `in_progress` → `completed` |
| `theory` | object | Theory progress |
| `examples` | object | Example walkthrough progress |
| `code` | object | Code writing progress |

## `theory` Object

| Field | Type | Description |
|-------|------|-------------|
| `mastered` | boolean | Theory mastered (≥ 75% correct answers) |
| `score` | number \| null | Percentage of correct answers (0–100) |
| `attempts` | number | Number of review attempts |
| `last_checked` | string \| null | Last review date |
| `notes` | string | Instructor comments |

## `examples` and `code` Objects

| Field | Type | Description |
|-------|------|-------------|
| `mastered` | boolean | Block mastered |
| `completed` | string[] | List of completed tasks |
| `attempts` | number | Number of attempts |
| `last_checked` | string \| null | Last review date |
| `notes` | string | Instructor comments |

## Status Transition Rules

- `not_started` → `in_progress`: student started the module.
- `in_progress` → `completed`: `theory.mastered`, `examples.mastered`, and `code.mastered` are all `true`.
- The next module unlocks only after the previous one is `completed`.
