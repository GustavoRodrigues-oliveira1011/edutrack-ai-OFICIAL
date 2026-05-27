// List all subjects
query subjects verb=GET {
  api_group = "subjects"

  input {
  }

  stack {
    db.query subject {
      where = $db.subject.user_id == $auth.id
      return = {type: "list"}
    } as $all_data
  }

  response = $all_data
}