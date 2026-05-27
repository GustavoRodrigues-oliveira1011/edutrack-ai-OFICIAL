## Context

The application currently has a `subjects` table and an `academic_tasks` table. Users need to search for subjects based on the subject name or if the subject has tasks that are currently overdue. The calculation for overdue tasks involves checking if a task is incomplete and past its due date. We want to leverage Python for this calculation to keep the logic aligned with other scripts (like `calculate_progress.py`), while exposing it through a new search endpoint in the `subjects` API.

## Goals / Non-Goals

**Goals:**
- Implement a search endpoint `GET /subjects/search` (or similar) that takes a query parameter.
- Implement Python logic (`scripts/filter_overdue_tasks.py`) to process tasks and determine if they are overdue.
- Integrate the Python script execution within the API endpoint logic.
- Return a unified list of subjects that match the name OR have overdue tasks.

**Non-Goals:**
- Modifying the existing GET /subjects endpoint directly (we will create a new dedicated search endpoint or adapt a specific query mechanism).
- Changing the schema of `subjects` or `academic_tasks`.

## Decisions

- **Endpoint Structure:** We will create a new endpoint (e.g., `GET /subjects/search`) that accepts parameters like `?query=math&include_overdue=true`.
- **Python Integration:** We will create a script `scripts/filter_overdue_tasks.py` that takes a JSON input of tasks and returns the IDs of subjects that have overdue tasks. The endpoint will:
  1. Query subjects matching the name `query`.
  2. Query all tasks for the user and pass them to the Python script.
  3. The Python script returns a list of subject IDs with overdue tasks.
  4. The endpoint merges the results (OR condition) and returns unique subjects.

## Risks / Trade-offs

- **Performance:** Fetching all tasks and passing them to a Python script could be slow for users with thousands of tasks.
  - *Mitigation:* The Python script should be optimized, or we could pass only incomplete tasks to the script.
- **Complexity:** Keeping the logic in Python instead of a direct SQL/DB query adds an integration layer.
  - *Mitigation:* We will keep the Python script simple and ensure robust JSON parsing.