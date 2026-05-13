## Why

O aluno precisa de uma forma de registrar e gerenciar suas obrigações acadêmicas (como lições, provas e trabalhos) vinculadas a cada disciplina, permitindo um acompanhamento claro de seus prazos e status.

## What Changes

- Criação da tabela de banco de dados `academic_tasks`.
- A tabela conterá os campos: `title`, `description`, `due_date`, `status`, `subject_id` (relacionamento com a tabela `subjects`) e `user_id` (relacionamento com a tabela `users` conforme as regras do EduTrack AI).

## Capabilities

### New Capabilities
- `academic-tasks-db`: Estrutura de banco de dados para gerenciar tarefas acadêmicas.

### Modified Capabilities

## Impact

- Banco de dados (Xano): Adição da nova tabela `academic_tasks` com chaves estrangeiras para `subjects` e `users`.