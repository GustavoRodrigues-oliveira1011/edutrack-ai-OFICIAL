## ADDED Requirements

### Requirement: Calculate Progress Percentage
The script SHALL compute the percentage of completed tasks relative to the total tasks provided.

#### Scenario: Normal calculation
- **WHEN** completed tasks are provided as 5 and total tasks as 10
- **THEN** the script computes the percentage as 50.0

#### Scenario: Zero total tasks
- **WHEN** total tasks are provided as 0
- **THEN** the script computes the percentage as 0.0 to handle division by zero gracefully

### Requirement: JSON Output format
The script SHALL output the result as a valid JSON string to standard output.

#### Scenario: Successful execution
- **WHEN** calculation is complete
- **THEN** output is printed in JSON format containing "completed", "total", and "percentage" fields, e.g., `{"completed": 5, "total": 10, "percentage": 50.0}`
