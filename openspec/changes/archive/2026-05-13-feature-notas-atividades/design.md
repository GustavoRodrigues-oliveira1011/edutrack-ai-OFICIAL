## Context

No sistema EduTrack AI, há a necessidade de permitir que professores registrem as notas de alunos em atividades acadêmicas específicas. Atualmente, os professores não possuem um meio para lançar essas notas no sistema e associá-las aos alunos. A solução será construída no backend Xano.

## Goals / Non-Goals

**Goals:**
- Criar a tabela `activity_grades` para armazenar as notas, relacionando a atividade, o aluno e a nota.
- Criar um endpoint API REST (`POST /activity_grades`) para inserção das notas pelo professor logado.
- Garantir a segurança filtrando/registrando operações de acordo com o `user_id` do usuário autenticado (professor).

**Non-Goals:**
- Desenvolver interfaces de frontend nesta etapa.
- Criar APIs de listagem (GET) que não foram explicitamente solicitadas.

## Decisions

- **Banco de Dados (Xano):** A tabela `activity_grades` utilizará `user_id` do usuário logado (professor) e referências necessárias como `student_id` (para o aluno que recebe a nota) e possivelmente `activity_id` ou nome da atividade, garantindo a associação correta e a segurança exigida nos padrões do projeto.
- **API Endpoint:** O endpoint será `POST /activity_grades` visando apenas o registro das notas.

## Risks / Trade-offs

- **Segurança:** Existe o risco de professores lançarem notas para alunos que não lecionam, o que pode ser mitigado com validações de relacionamento futuramente ou garantindo que o `user_id` autenticado fique sempre registrado.
