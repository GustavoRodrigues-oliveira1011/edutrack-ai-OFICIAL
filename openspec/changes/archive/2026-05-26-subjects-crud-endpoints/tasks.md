## 1. Subjects Endpoints Setup

- [x] 1.1 Verificar e validar o schema do Xano em `.xs` para o endpoint POST (`apis/subjects/4000001_subjects_POST.xs`), garantindo que o `user_id` é injetado a partir da autenticação, ignorando payload.
- [x] 1.2 Verificar e validar o endpoint GET List (`apis/subjects/4000002_subjects_GET.xs`), adicionando o filtro para retornar apenas registros onde `user_id = auth.id`.
- [x] 1.3 Verificar e validar o endpoint GET by ID (`apis/subjects/4000003_subjects_id_GET.xs`), assegurando que a query filtra por `user_id = auth.id` (ou retorna 404/403 em caso de falha).
- [x] 1.4 Verificar e validar o endpoint PUT/PATCH (`apis/subjects/4000004_subjects_id_PUT.xs`), garantindo que o update requer match do `user_id` e retorna erro caso o registro não pertença ao usuário.
- [x] 1.5 Verificar e validar o endpoint DELETE (`apis/subjects/4000005_subjects_id_DELETE.xs`), aplicando a mesma regra do PUT/PATCH para garantir que apenas o dono do registro pode apagá-lo.

## 2. Validation & Testing

- [x] 2.1 Revisar cada arquivo modificado sob `apis/subjects/` para assegurar que não haja dependências faltantes ou variáveis de autenticação referenciadas incorretamente.
- [x] 2.2 Se possível, configurar testes locais ou descrever cenários de teste manuais para validação de tenant isolation.