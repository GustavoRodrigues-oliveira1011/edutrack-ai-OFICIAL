# activity-grades Specification
## Purpose
Define the database structure and API endpoints for managing activity grades in EduTrack AI, permitindo que professores lancem notas para os alunos.

## ADDED Requirements

### Requirement: Create activity_grades table
The system SHALL store grade information for specific activities assigned to students.

#### Scenario: Teacher assigns a grade
- **WHEN** a teacher creates a new activity grade
- **THEN** the system stores it associated with the teacher's `user_id` and the `student_id`

### Requirement: Create POST /activity_grades API
The system SHALL provide a RESTful POST endpoint to allow teachers to record grades.

#### Scenario: Teacher posts a new grade
- **WHEN** a teacher sends a valid POST request to `/activity_grades` with grade details
- **THEN** the system saves the grade and returns a success response