## 1. Configuração do Banco de Dados Xano

- [x] 1.1 Criar a tabela `subjects` no banco de dados Xano.
- [x] 1.2 Adicionar os campos à tabela `subjects` conforme a especificação: `name` (text, obrigatório), `description` (text), `teacher` (text).
- [x] 1.3 Adicionar o campo de referência de tabela `user_id` na tabela `subjects`, vinculando-o à tabela `user` e tornando-o obrigatório.
- [x] 1.4 Habilitar a exclusão em cascata na relação `user` -> `subjects` para que as disciplinas de um usuário sejam removidas se o usuário for excluído.

## 2. Implementação dos Endpoints da API

- [x] 2.1 Criar um novo grupo de APIs em Xano chamado `subjects`.
- [x] 2.2 Implementar o endpoint `POST /subjects`:
    - Adicionar a lógica para receber `name`, `description`, `teacher`.
    - Atribuir automaticamente o `user_id` do usuário autenticado.
    - Retornar o registro criado com status 201.
- [x] 2.3 Implementar o endpoint `GET /subjects`:
    - Adicionar a lógica para consultar todos os `subjects` onde o `user_id` corresponde ao do usuário autenticado.
    - Retornar a lista de registros com status 200.
- [x] 2.4 Implementar o endpoint `GET /subjects/{id}`:
    - Adicionar a lógica para buscar um `subject` pelo seu `id`.
    - Implementar a verificação de propriedade (o `user_id` do `subject` deve corresponder ao do usuário autenticado).
    - Retornar o registro encontrado ou um erro de autorização/não encontrado.
- [x] 2.5 Implementar o endpoint `PUT /subjects/{id}`:
    - Adicionar a lógica para buscar um `subject` pelo seu `id`.
    - Implementar a verificação de propriedade.
    - Atualizar os campos com os novos dados fornecidos.
    - Retornar o registro atualizado.
- [x] 2.6 Implementar o endpoint `DELETE /subjects/{id}`:
    - Adicionar a lógica para buscar um `subject` pelo seu `id`.
    - Implementar a verificação de propriedade.
    - Excluir o registro.
    - Retornar um status 204.

## 3. Segurança e Validação

- [x] 3.1 Revisar todos os endpoints da API `subjects` para garantir que a autenticação de usuário seja obrigatória.
- [x] 3.2 Testar a lógica de autorização para confirmar que um usuário não pode ler, atualizar ou excluir disciplinas de outro usuário.
- [x] 3.3 Adicionar validação de entrada no endpoint `POST` para garantir que o campo `name` não seja nulo ou vazio.
