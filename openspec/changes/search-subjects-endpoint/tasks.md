## 1. Scripts

- [x] 1.1 Create `scripts/filter_overdue_tasks.py` to parse JSON tasks and return a list of subject IDs with overdue tasks.
- [x] 1.2 Test the Python script with a sample JSON payload to ensure accurate logic.

## 2. API Endpoints

- [ ] 2.1 Create a new Xano API endpoint `GET /subjects/search` in `apis/subjects/`.
- [ ] 2.2 Configure the endpoint to accept query parameters (e.g., `query`).
- [ ] 2.3 Implement the logic to fetch subjects matching the name query.
- [ ] 2.4 Implement the logic to fetch the user's tasks and call the Python script.
- [ ] 2.5 Merge the results from the name query and the overdue task script (OR condition) and return the unique list of subjects.