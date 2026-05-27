query subjects verb=POST {
  api_group = "subjects"

  input {
    text name
    text description
    text teacher
  }

  stack {
    db.add subject {
      data = {
        name       : $input.name
        description: $input.description
        teacher    : $input.teacher
        user_id    : $auth.id
      }
    } as $new_subject
  }

  response = $new_subject
}