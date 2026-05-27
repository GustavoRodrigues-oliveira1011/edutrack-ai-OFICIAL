## 1. Setup

- [x] 1.1 Criar a pasta `scripts` na raiz do projeto (se ela ainda não existir).
- [x] 1.2 Criar o arquivo `scripts/calculate_progress.py`.

## 2. Core Implementation

- [x] 2.1 Adicionar os imports necessários (`argparse` e `json`).
- [x] 2.2 Configurar os argumentos de linha de comando `--completed` e `--total` usando o tipo `int`.
- [x] 2.3 Implementar a lógica principal: verificar se `--total` é zero (retornar 0.0 neste caso) e, se não, calcular a divisão de `completed` por `total` multiplicada por 100.
- [x] 2.4 Estruturar o resultado em um dicionário com chaves `completed`, `total` e `percentage`.
- [x] 2.5 Converter o dicionário para string JSON e usar `print()` para enviar a saída.

## 3. Testing & Validation

- [x] 3.1 Executar manualmente o script passando `--completed 5 --total 10` e validar a saída JSON (esperado: `{"completed": 5, "total": 10, "percentage": 50.0}`).
- [x] 3.2 Executar manualmente o script passando `--completed 0 --total 0` e validar a saída JSON (esperado: `{"completed": 0, "total": 0, "percentage": 0.0}`).