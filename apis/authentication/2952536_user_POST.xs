// Add user record
query user verb=POST {
  api_group = "Authentication"

  input {
    dblink {
      table = ""
    }
  }

  stack {
    db.add "" {
      data = {created_at: "now"}
    } as $user
  }

  response = $user
}