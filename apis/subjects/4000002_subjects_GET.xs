// List all subjects
query subjects verb=GET {
  api_group = "subjects"

  input {
  }

  stack {
    db.query subject {
      return = {type: "list"}
    } as $all_data
  }

  response = $all_data
}