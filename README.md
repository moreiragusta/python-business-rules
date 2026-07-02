# Python Business Rules

Projeto de estudos com regras de negócio em Python e testes automatizados usando pytest.

## Funcionalidades

- Cálculo de preço com desconto
- Validação de preço negativo
- Validação de desconto negativo
- Validação de desconto maior que 100%
- Arredondamento do resultado para duas casas decimais

## Tecnologias usadas

- Python
- Pytest

## Como instalar

Crie o ambiente virtual:

```bash
python -m venv .venv

Ative o ambiente virtual no Windows:

.venv\Scripts\activate

Instale as dependências:

pip install -r requirements-dev.txt
Como executar os testes

No PowerShell:

$env:PYTHONPATH="src"
pytest

No CMD:

set PYTHONPATH=src
pytest