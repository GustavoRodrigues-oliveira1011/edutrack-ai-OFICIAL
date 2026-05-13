table academic_tasks {
  description = "Tabela para armazenar as atividades acadêmicas (lições, provas, trabalhos) vinculadas às disciplinas."

  // Campos principais
  text title { description = "Título da atividade acadêmica" }
  text description { description = "Descrição detalhada da atividade" }
  timestamp due_date { description = "Data de entrega ou data da prova" }
  text status?="pending" { description = "Status da atividade (ex: pending, completed)" }

  // Relacionamentos
  table_reference subject_id {
    table = "subjects"
    description = "Referência à disciplina a qual esta atividade pertence"
  }

  table_reference user_id {
    table = "users"
    description = "Referência ao usuário logado, para isolamento de dados"
  }
}
