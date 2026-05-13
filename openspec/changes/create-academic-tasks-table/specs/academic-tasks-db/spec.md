# academic-tasks-db Specification

## Purpose
Define the database structure for managing academic tasks in EduTrack AI.

## ADDED Requirements

### Requirement: Create academic_tasks table
The system SHALL store academic task information linked to both subjects and users.

#### Scenario: Database schema implementation
- **WHEN** the academic_tasks table is created
- **THEN** it must contain the fields: title, description, due_date, status, subject_id, and user_id