// Update user record
query "user/{user_id}" verb=PUT {
  api_group = "Authentication"

  input {
    int user_id? filters=min:1
    dblink {
      table = ""
    }
  }

  stack {
    db.edit "" {
      field_name = "id"
      field_value = $input.user_id
      data = {}
    } as $model
  }

  response = $model
}