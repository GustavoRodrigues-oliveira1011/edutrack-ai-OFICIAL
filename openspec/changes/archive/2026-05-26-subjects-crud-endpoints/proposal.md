## Why

Para permitir que a aplicação gerencie disciplinas (subjects), precisamos de endpoints de API para realizar as operações CRUD padrão. É vital para a segurança e privacidade da aplicação que esses endpoints garantam que os usuários só possam ler, editar e deletar seus próprios dados.

## What Changes

- Definição dos endpoints da API de subjects: POST (criar), GET (listar todos), GET by ID (detalhes), PATCH/PUT (atualizar), DELETE (remover).
- Adição de regras de autorização em todos os endpoints para validar o `user_id` e garantir o isolamento dos dados por usuário.

## Capabilities

### New Capabilities
- `subjects-api`: Endpoints CRUD para gerenciamento de disciplinas com isolamento de dados por usuário.

### Modified Capabilities

## Impact

- **Segurança**: Garante privacidade dos dados entre diferentes usuários.
- **Frontend**: Permite que a interface do usuário gerencie disciplinas via API.
