## Context

O sistema necessita de uma forma padronizada e simples para calcular a porcentagem de progresso de atividades ou tarefas (concluídas vs total). A abordagem escolhida é criar um utilitário em Python que receba esses valores e retorne o resultado em JSON, permitindo sua utilização por CLI ou como subprocesso por outras camadas do sistema.

## Goals / Non-Goals

**Goals:**
- Criar o script `scripts/calculate_progress.py`.
- Aceitar os valores de `completed` (concluídas) e `total` via argumentos de linha de comando.
- Retornar um output em formato JSON para a saída padrão (stdout).
- Lidar com casos extremos, como total de tarefas igual a zero.

**Non-Goals:**
- Integração com banco de dados; o script atuará apenas como uma função pura (recebe os dados, processa, retorna JSON).

## Decisions

- **Mecanismo de Input**: Utilizaremos a biblioteca padrão `argparse` para receber `--completed` e `--total`. É robusto e gera mensagens de erro caso os inputs estejam ausentes ou incorretos.
- **Divisão por zero**: Quando `--total` for 0, a porcentagem será 0.0 para refletir de maneira segura no frontend.

## Risks / Trade-offs

- **Risco**: Tipos de dados incorretos passados nos argumentos.
  **Mitigação**: `argparse` configurado com `type=int` garantirá que os valores sejam numéricos.