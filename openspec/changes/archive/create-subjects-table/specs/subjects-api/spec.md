## ADDED Requirements

### Requirement: Criar Disciplina
O sistema DEVE fornecer um endpoint de API para criar uma nova disciplina.

#### Scenario: Criação com Sucesso
- **WHEN** uma solicitação `POST` for enviada para `/subjects` com dados válidos (`name`) e um token de autenticação
- **THEN** o sistema DEVE criar um novo registro de `subject` associado ao usuário autenticado e retornar um status `201 Created` com os dados da nova disciplina.

#### Scenario: Tentativa de Criação sem Autenticação
- **WHEN** uma solicitação `POST` for enviada para `/subjects` sem um token de autenticação
- **THEN** o sistema DEVE retornar um erro `401 Unauthorized`.

### Requirement: Listar Disciplinas
O sistema DEVE fornecer um endpoint de API para listar todas as disciplinas de um usuário.

#### Scenario: Listagem com Sucesso
- **WHEN** uma solicitação `GET` for enviada para `/subjects` com um token de autenticação
- **THEN** o sistema DEVE retornar um status `200 OK` e uma lista de todos os `subjects` pertencentes ao usuário autenticado.

#### Scenario: Listagem de Outro Usuário
- **WHEN** um usuário autenticado tentar listar as disciplinas de outro usuário
- **THEN** o sistema DEVE retornar apenas as disciplinas do usuário autenticado.

### Requirement: Obter Detalhes da Disciplina
O sistema DEVE fornecer um endpoint para obter os detalhes de uma única disciplina.

#### Scenario: Obtenção com Sucesso
- **WHEN** uma solicitação `GET` for enviada para `/subjects/{id}` com o ID de uma disciplina pertencente ao usuário
- **THEN** o sistema DEVE retornar um status `200 OK` e os dados completos da disciplina.

#### Scenario: Tentativa de Obter Disciplina de Outro Usuário
- **WHEN** uma solicitação `GET` for enviada para `/subjects/{id}` com o ID de uma disciplina que não pertence ao usuário
- **THEN** o sistema DEVE retornar um erro `403 Forbidden` ou `404 Not Found`.

### Requirement: Atualizar Disciplina
O sistema DEVE fornecer um endpoint para atualizar uma disciplina existente.

#### Scenario: Atualização com Sucesso
- **WHEN** uma solicitação `PUT` for enviada para `/subjects/{id}` com dados válidos e o ID de uma disciplina pertencente ao usuário
- **THEN** o sistema DEVE atualizar o registro da disciplina e retornar um status `200 OK` com os dados atualizados.

#### Scenario: Tentativa de Atualizar Disciplina de Outro Usuário
- **WHEN** uma solicitação `PUT` for enviada para `/subjects/{id}` com o ID de uma disciplina que não pertence ao usuário
- **THEN** o sistema DEVE retornar um erro `403 Forbidden` ou `404 Not Found`.

### Requirement: Excluir Disciplina
O sistema DEVE fornecer um endpoint para excluir uma disciplina.

#### Scenario: Exclusão com Sucesso
- **WHEN** uma solicitação `DELETE` for enviada para `/subjects/{id}` com o ID de uma disciplina pertencente ao usuário
- **THEN** o sistema DEVE excluir o registro da disciplina e retornar um status `204 No Content`.

#### Scenario: Tentativa de Excluir Disciplina de Outro Usuário
- **WHEN** uma solicitação `DELETE` for enviada para `/subjects/{id}` com o ID de uma disciplina que não pertence ao usuário
- **THEN** o sistema DEVE retornar um erro `4e-05 Forbidden` ou `404 Not Found`.
