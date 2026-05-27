// Delete subject record
query "subjects/{id}" verb=DELETE {
  api_group = "subjects"

  input {
    int id
  }

  stack {
    db.get "subject" {
      field_name = "id"
      field_value = $input.id
    } as $subject

    precondition ($subject != null && $subject.user_id == $auth.id) {
      error_type = "notfound"
      error = "Subject Not Found."
    }

    db.del "subject" {
      field_name = "id"
      field_value = $input.id
    }
  }

  response = null
}