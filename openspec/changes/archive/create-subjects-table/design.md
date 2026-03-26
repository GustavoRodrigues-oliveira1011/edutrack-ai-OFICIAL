## Context

O sistema atual, construído em Xano, não possui uma tabela ou APIs para gerenciar disciplinas acadêmicas (`subjects`). O `proposal.md` estabeleceu a necessidade de criar essa funcionalidade para permitir que os usuários rastreiem suas disciplinas. Este documento de design detalha a abordagem técnica para implementar a tabela de `subjects` e as APIs CRUD correspondentes dentro do ambiente Xano existente.

## Goals / Non-Goals

**Goals:**
- Definir e criar o esquema da tabela `subjects` no banco de dados Xano.
- Implementar um novo grupo de APIs (`/subjects`) para fornecer funcionalidade CRUD completa para as disciplinas.
- Garantir que apenas usuários autenticados possam criar e gerenciar *suas próprias* disciplinas, aplicando controle de acesso baseado em propriedade.
- Estabelecer uma base sólida para futuras funcionalidades que possam depender dos dados das disciplinas.

**Non-Goals:**
- Implementação de qualquer componente de frontend. O foco é exclusivamente no backend.
- Funcionalidades colaborativas, como compartilhamento de disciplinas entre usuários ou múltiplos professores por disciplina.
- Geração de relatórios ou análises sobre os dados das disciplinas.

## Decisions

1.  **Plataforma**: A implementação será inteiramente realizada em **Xano**, em conformidade com a stack tecnológica existente do projeto.

2.  **Modelo de Dados (Tabela `subjects`)**:
    - Uma nova tabela chamada `subjects` será criada.
    - **Relacionamento de Propriedade**: Para vincular cada disciplina a um usuário, um campo `user_id` será adicionado à tabela `subjects`. Este campo será uma **referência de tabela** (`table reference`) para a tabela `user`. Esta abordagem de chave estrangeira direta é preferível a uma tabela de junção separada, pois simplifica o esquema para o relacionamento claro de um-para-muitos (um usuário tem muitas disciplinas).
    - **Schema Inicial**:
        - `id` (gerado por Xano)
        - `created_at` (gerado por Xano)
        - `name` (text)
        - `description` (text)
        - `teacher` (text)
        - `user_id` (table reference to `user`)

3.  **Estrutura da API (`/subjects`)**:
    - Um novo grupo de APIs chamado `subjects` será criado para organizar os endpoints.
    - Serão implementados os seguintes endpoints RESTful:
        - `POST /subjects`: Cria uma nova disciplina. O `user_id` do usuário autenticado será atribuído automaticamente.
        - `GET /subjects`: Lista todas as disciplinas pertencentes ao usuário autenticado.
        - `GET /subjects/{id}`: Obtém os detalhes de uma única disciplina.
        - `PUT /subjects/{id}`: Atualiza uma disciplina existente.
        - `DELETE /subjects/{id}`: Exclui uma disciplina.

4.  **Autenticação e Autorização**:
    - **Autenticação**: Todos os endpoints no grupo de API `subjects` exigirão um token de autenticação de usuário válido.
    - **Autorização**: A lógica de autorização será implementada diretamente nos endpoints da API.
        - Para `GET /subjects/{id}`, `PUT /subjects/{id}` e `DELETE /subjects/{id}`, o primeiro passo na lógica da função será verificar se o `user_id` do registro `subject` solicitado corresponde ao `id` do usuário autenticado (`auth.id`).
        - Se não houver correspondência, a API retornará um erro `403 Forbidden` ou `404 Not Found` para evitar a enumeração de recursos.

## Risks / Trade-offs

- **Risco**: Acoplamento forte com a plataforma Xano.
  - **Mitigação**: Este é um risco aceito, pois todo o backend do projeto já está consolidado em Xano. A consistência da plataforma é mais valiosa nesta fase.
- **Trade-off**: O modelo de dados inicial não oferece suporte a cenários de múltiplos proprietários ou colaboração.
  - **Justificativa**: Simplifica a implementação inicial. Se a colaboração se tornar um requisito no futuro, o esquema pode ser estendido com uma tabela de junção (ex: `subject_members`). A abordagem atual atende perfeitamente ao requisito de propriedade individual.
