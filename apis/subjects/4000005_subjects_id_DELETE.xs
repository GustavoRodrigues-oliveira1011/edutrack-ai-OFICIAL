// Delete subject record
query "subjects/{id}" verb=DELETE {
  api_group = "subjects"

  input {
    int id
  }

  stack {
    db.del "subject" {
      field_name = "id"
      field_value = $input.id
    }
  }

  response = null
}