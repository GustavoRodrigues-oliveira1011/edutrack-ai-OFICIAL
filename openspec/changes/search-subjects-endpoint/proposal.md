## Why

Users need a powerful search functionality to quickly find specific subjects either by their name or by identifying subjects that require immediate attention due to overdue tasks. This enables better time management and focus on pending work.

## What Changes

- Create a new search endpoint for the `subjects` API.
- Implement filtering logic to match subjects by name (partial or exact match).
- Create a Python script in `scripts/` (e.g., `check_overdue_tasks.py`) to evaluate overdue logic for tasks.
- Integrate the Python script execution into the Xano endpoint.
- Combine the filters using an OR condition so subjects matching either criteria (name match OR has overdue tasks) are returned.

## Capabilities

### New Capabilities
- `search-subjects-api`: Capability to search and filter subjects based on name or presence of overdue tasks using Python integration.

### Modified Capabilities

## Impact

- **APIs**: New search endpoint in the `subjects` API group.
- **Scripts**: New Python script for overdue tasks calculation.
- **Database**: Reads from `subjects` and `academic_tasks` tables.