// Tabela de disciplinas vinculada ao usuário
table subject {
  auth = false

  schema {
    int id
    timestamp created_at?=now
    text name filters=trim
    text? description filters=trim
    text? teacher filters=trim
    int user_id
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
  ]
}