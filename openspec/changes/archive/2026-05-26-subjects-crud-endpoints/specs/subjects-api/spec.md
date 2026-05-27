## ADDED Requirements

### Requirement: Isolate Subject Creation
The POST endpoint SHALL automatically assign the `user_id` of the currently authenticated user to the newly created subject. It MUST ignore any `user_id` passed in the request body.

#### Scenario: User creates a subject
- **WHEN** an authenticated user sends a POST request with subject details
- **THEN** the subject is created and associated exclusively with their user ID

### Requirement: Isolate Subject Listing
The GET endpoints (List) SHALL return only subjects where `user_id` matches the currently authenticated user's ID.

#### Scenario: User lists subjects
- **WHEN** an authenticated user requests the list of subjects
- **THEN** the system returns an array containing only their subjects, hiding all others

### Requirement: Isolate Subject Details
The GET by ID endpoint SHALL return the subject details only if the subject belongs to the currently authenticated user.

#### Scenario: User requests own subject
- **WHEN** user requests a subject ID they own
- **THEN** the system returns the subject details

#### Scenario: User requests foreign subject
- **WHEN** user requests a subject ID belonging to another user
- **THEN** the system returns a 404 Not Found or 403 Forbidden error

### Requirement: Isolate Subject Updates
The PATCH/PUT endpoint SHALL allow updates only to subjects owned by the currently authenticated user.

#### Scenario: User updates foreign subject
- **WHEN** user attempts to update a subject belonging to another user
- **THEN** the system prevents the update and returns an error (404/403)

### Requirement: Isolate Subject Deletion
The DELETE endpoint SHALL allow deletion only of subjects owned by the currently authenticated user.

#### Scenario: User deletes foreign subject
- **WHEN** user attempts to delete a subject belonging to another user
- **THEN** the system prevents deletion and returns an error (404/403)