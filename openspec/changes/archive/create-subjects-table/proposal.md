## Why

Atualmente, não há um local para os usuários armazenarem ou gerenciarem suas disciplinas acadêmicas. A adição de uma tabela de `subjects` é o primeiro passo para permitir que os usuários acompanhem seu progresso acadêmico, gerenciem informações relacionadas aos cursos e habilitem futuras funcionalidades de automação e análise.

## What Changes

- Uma nova tabela de banco de dados chamada `subjects` será criada.
- A tabela `subjects` incluirá campos como `name`, `description`, `teacher`, e uma referência ao `user_id` para definir a propriedade.
- Novos endpoints de API serão criados para operações CRUD (Criar, Ler, Atualizar, Excluir) na tabela `subjects`.
- Apenas o usuário proprietário (ou um administrador) poderá gerenciar suas próprias disciplinas.

## Capabilities

### New Capabilities
- `subjects-db`: Define o esquema da tabela `subjects`, incluindo campos, tipos de dados e relacionamentos.
- `subjects-api`: Define os endpoints da API para criar, ler, atualizar e excluir `subjects`.

### Modified Capabilities
- Nenhuma

## Impact

- **Banco de Dados**: Uma nova tabela (`subjects`) será adicionada ao banco de dados Xano.
- **API**: Um novo grupo de APIs com endpoints CRUD será criado em Xano.
- **Frontend**: O frontend precisará ser atualizado posteriormente para consumir as novas APIs e gerenciar as disciplinas.
- **Autenticação**: Os endpoints da API exigirão autenticação para garantir que os usuários só possam acessar suas próprias disciplinas.
