## Context

O sistema EduTrack AI precisa de uma nova tabela chamada `academic_tasks` para armazenar as atividades acadêmicas dos alunos, vinculando-as às disciplinas existentes e aos próprios usuários por questões de segurança e multi-tenancy.

## Goals / Non-Goals

**Goals:**
- Criar a tabela `academic_tasks` no banco de dados (Xano).
- Configurar os campos: `title`, `description`, `due_date` e `status`.
- Estabelecer as chaves estrangeiras: `subject_id` e `user_id`.

**Non-Goals:**
- Criação de APIs (CRUD) para a tabela neste momento.
- Integração com o frontend.

## Decisions

- **Chave primária:** A tabela utilizará o `id` padrão do Xano.
- **Tipos de dados:** `title` (text), `description` (text), `due_date` (timestamp/date), `status` (text).
- **Relacionamentos:** `subject_id` (table reference) e `user_id` (table reference), para garantir o escopo dos dados por aluno, conforme exigido pelas diretrizes de segurança do projeto.

## Risks / Trade-offs

- N/A.
