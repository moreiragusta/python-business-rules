# Python Business Rules

Projeto de estudos com regras de negócio em Python e testes automatizados usando `pytest`.

O objetivo deste repositório é praticar lógica de programação aplicada, organização de código, validação de regras de negócio, testes automatizados e versionamento com Git/GitHub.

## Funcionalidades

### Cálculo de preço com desconto

* Validação de preço negativo
* Validação de desconto negativo
* Validação de desconto maior que 100%
* Arredondamento do resultado para duas casas decimais

### Cálculo de juros simples

* Validação de valor inicial negativo
* Validação de taxa percentual negativa
* Validação de quantidade de meses negativa
* Arredondamento do resultado para duas casas decimais

### Cálculo de multa por atraso

- Retorno do valor original quando não há atraso
- Aplicação de multa percentual quando há atraso
- Validação de valor original negativo
- Validação de percentual de multa negativo
- Validação de dias de atraso negativo
- Arredondamento do resultado para duas casas decimais

## Tecnologias usadas

* Python
* Pytest
* Git
* GitHub

## Estrutura do projeto

```text
python-business-rules/
├── src/
│   └── business_rules/
│       ├── __init__.py
│       ├── descontos.py
│       ├── juros.py
│       └── multas.py
├── tests/
│   ├── test_descontos.py
│   ├── test_juros.py
│   └── test_multas.py
├── README.md
├── pyproject.toml
├── requirements-dev.txt
└── .gitignore
```

## Como instalar

Clone o repositório:

```bash
git clone https://github.com/moreiragusta/python-business-rules.git
```

Acesse a pasta do projeto:

```bash
cd python-business-rules
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências de desenvolvimento:

```bash
pip install -r requirements-dev.txt
```

## Como executar os testes

Execute:

```bash
pytest
```

Se tudo estiver correto, o terminal deverá exibir os testes passando.

Exemplo:

```text
16 passed
```

## Regras de negócio implementadas

### Cálculo de desconto

A função `calcular_preco_com_desconto` recebe um preço e um percentual de desconto, valida os dados de entrada e retorna o preço final com duas casas decimais.

Exemplo:

```python
from business_rules.descontos import calcular_preco_com_desconto

preco_final = calcular_preco_com_desconto(100, 10)

print(preco_final)
# 90
```

### Cálculo de juros simples

A função `calcular_juros_simples` recebe um valor inicial, uma taxa percentual e uma quantidade de meses. Depois, calcula o valor final usando juros simples.

Exemplo:

```python
from business_rules.juros import calcular_juros_simples

valor_final = calcular_juros_simples(1000, 2, 3)

print(valor_final)
# 1060
```

## Cenários testados

Os testes automatizados verificam:

* cálculo correto de desconto
* desconto de 0%
* desconto de 100%
* erro para preço negativo
* erro para desconto negativo
* erro para desconto maior que 100%
* cálculo correto de juros simples
* juros com taxa de 0%
* juros com 0 meses
* erro para valor inicial negativo
* erro para taxa percentual negativa
* erro para quantidade de meses negativa
* arredondamento para duas casas decimais

## Decisões técnicas

O código da aplicação foi separado na pasta `src/` para manter uma organização mais próxima de projetos profissionais.

Os testes foram separados na pasta `tests/`, evitando misturar código de produção com código de teste.

As funções não utilizam `input()` nem `print()`, porque regras de negócio devem ser independentes da interface. Isso facilita a manutenção, a reutilização e os testes automatizados.

## Melhorias futuras

* Adicionar cálculo de parcelas
* Adicionar validação de CPF
* Adicionar cálculo de multa e juros por atraso
* Adicionar novas regras financeiras
* Melhorar a documentação dos módulos
* Adicionar cobertura de testes
* Configurar execução automatizada dos testes com GitHub Actions
