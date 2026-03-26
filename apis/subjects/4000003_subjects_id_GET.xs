// Get subject record
query "subjects/{id}" verb=GET {
  api_group = "subjects"

  input {
    int id
  }

  stack {
    db.get "subject" {
      field_name = "id"
      field_value = $input.id
    } as $subject

    precondition ($subject != null) {
      error_type = "notfound"
      error = "Subject Not Found."
    }
  }

  response = $subject
}