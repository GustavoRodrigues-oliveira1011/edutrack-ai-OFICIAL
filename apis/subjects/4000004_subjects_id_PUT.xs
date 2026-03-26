query "subjects/{id}" verb=PUT {
  api_group = "subjects"

  input {
    int id
    text name
    text description
    text teacher
  }

  stack {
    db.edit subject {
      field_name = "id"
      field_value = $input.id
      data = {
        name       : $input.name
        description: $input.description
        teacher    : $input.teacher
      }
    } as $updated_subject
  }

  response = $updated_subject
}