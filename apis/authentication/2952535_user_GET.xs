// Query all user records
query user verb=GET {
  api_group = "Authentication"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $user
  }

  response = $user
}