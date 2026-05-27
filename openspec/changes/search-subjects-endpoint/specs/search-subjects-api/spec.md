## ADDED Requirements

### Requirement: Search Subjects by Name or Overdue Tasks
The system SHALL provide a search endpoint for subjects that filters results based on a provided query string matching the subject's name, or if the subject has any associated academic tasks that are overdue. The endpoint SHALL integrate a Python script to evaluate the overdue task logic.

#### Scenario: Search by subject name
- **WHEN** the user provides a search query that matches a subject's name partially or exactly
- **THEN** the endpoint returns a list of subjects matching the name

#### Scenario: Search for subjects with overdue tasks
- **WHEN** the user provides a search query to filter for overdue tasks (e.g., query indicates overdue filter, or the query is evaluated by the Python script to find overdue items) and subjects have tasks where the due date is in the past and status is not complete
- **THEN** the endpoint returns the subjects containing those overdue tasks

#### Scenario: Search by both name and overdue tasks (OR condition)
- **WHEN** the user provides a search query and the system evaluates both conditions: the name matches the query OR the subject has overdue tasks
- **THEN** the endpoint returns subjects that satisfy at least one of the conditions