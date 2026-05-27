## Why

É necessário calcular a porcentagem de progresso das atividades (atividades concluídas em relação ao total de atividades) de forma programática. Este script permitirá automatizar o cálculo e disponibilizar o resultado em formato JSON para fácil integração com o front-end ou outras partes do sistema.

## What Changes

- Criação de um novo script Python `scripts/calculate_progress.py`.
- O script deverá aceitar dados de entrada (provavelmente via stdin, argumentos ou arquivo), calcular a taxa de conclusão e formatar a saída como um objeto JSON.

## Capabilities

### New Capabilities
- `progress-calculation`: Script Python para calcular a porcentagem de progresso de tarefas concluídas vs total e retornar a saída em JSON.

### Modified Capabilities

## Impact

- **Sistemas afetados**: Novos fluxos ou endpoints que precisarem apresentar métricas de progresso poderão chamar este script.
- **Dependências**: Requer ambiente de execução Python configurado.
