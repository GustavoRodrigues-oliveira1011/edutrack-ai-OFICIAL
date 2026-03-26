## ADDED Requirements

### Requirement: Tabela de Disciplinas
O sistema DEVE ter uma tabela de banco de dados chamada `subjects` para armazenar informações sobre as disciplinas acadêmicas.

#### Scenario: Definição do Esquema da Tabela
- **WHEN** a tabela `subjects` for inspecionada
- **THEN** ela DEVE conter as seguintes colunas com os tipos de dados especificados:
    - `id`: Integer (PK, auto-increment)
    - `created_at`: Timestamp
    - `name`: Text (obrigatório)
    - `description`: Text (opcional)
    - `teacher`: Text (opcional)
    - `user_id`: Relação (FK para a tabela `user`, obrigatório)

### Requirement: Relação de Propriedade
A tabela `subjects` DEVE ter uma relação com a tabela `user` para definir a propriedade.

#### Scenario: Vínculo com o Usuário
- **WHEN** um novo registro de `subject` for criado
- **THEN** o campo `user_id` DEVE ser preenchido com o ID do usuário que criou a disciplina.

#### Scenario: Integridade Referencial
- **WHEN** um `user` for excluído
- **THEN** todos os `subjects` associados a esse `user_id` DEVEM ser excluídos (deleção em cascata).
