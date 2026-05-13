## Why

Atualmente não há um mecanismo para que os professores possam registrar as notas dos alunos em atividades específicas. Essa funcionalidade é essencial para o acompanhamento do desempenho acadêmico e compõe a avaliação contínua no EduTrack AI.

## What Changes

- Criação de uma tabela para armazenar as notas das atividades (`activity_grades`).
- Criação de uma API para permitir a inserção de notas pelos professores.

## Capabilities

### New Capabilities
- `activity-grades`: Gerenciamento e armazenamento das notas de atividades específicas dos alunos.

### Modified Capabilities

## Impact

- Banco de dados: nova tabela `activity_grades`.
- APIs: novo endpoint de lançamento de notas.
