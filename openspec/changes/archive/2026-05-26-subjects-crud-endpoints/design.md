## Context

O backend atualmente usa Xano (arquivos `.xs`) e possui o grupo de API `subjects`. Precisamos garantir que os endpoints de CRUD (POST, GET, GET by ID, PATCH, DELETE) para a tabela `subjects` estejam implementados corretamente e reforcem o isolamento de dados por locatário (tenant/user), de modo que um usuário autenticado possa visualizar e manipular apenas os dados que ele mesmo criou.

## Goals / Non-Goals

**Goals:**
- Projetar a segurança dos endpoints de `subjects` (POST, GET, GET by ID, PATCH, DELETE).
- Garantir que toda query ao banco ou inserção inclua/valide o `user_id` vinculado ao token de autenticação atual do usuário.

**Non-Goals:**
- Alterar as definições de schema da tabela `subjects` além de possivelmente garantir que a coluna `user_id` seja o elo de relacionamento correto.
- Refatorar a autenticação global; assumimos que o middleware/autenticação padrão já fornece o `user_id` autenticado.

## Decisions

- **Isolamento via `user_id`:** Em vez de usar permissões complexas, adicionaremos uma cláusula `WHERE user_id = auth.id` (ou equivalente no Xano) nas operações de GET, GET by ID, PATCH e DELETE. Para o POST, o `user_id` será preenchido automaticamente com o ID do usuário logado, em vez de aceitar isso via payload.
- **Validação Antecipada (Fail Fast):** Se uma operação como PATCH ou DELETE não encontrar o registro pertencente ao usuário, a API retornará 404 (Not Found) ou 403 (Forbidden) imediatamente, não expondo a existência de registros de terceiros.

## Risks / Trade-offs

- **Risco:** Falha em aplicar o filtro `user_id` em um novo endpoint criado no futuro.
  **Mitigação:** Documentar esta regra claramente e adicionar testes automatizados ou cenários nas specs para validar o acesso não autorizado.