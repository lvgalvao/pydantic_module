# Pydantic Data Validation Project

## Overview

Este projeto utiliza a biblioteca Pydantic para efetuar validações em registros de vendas antes de sua persistência, garantindo integridade e conformidade.

## Como funciona?

1. Definimos uma classe `SalesRecord` que representa um registro de venda.
2. Esta classe utiliza várias validações, desde validações simples até validações personalizadas.

## Validations:

- **E-mail**: Valida automaticamente os e-mails.
- **Fornecedores**: Garante que apenas fornecedores da lista são aceitos.
- **Valor da Venda**: Garante um intervalo aceitável para o valor da venda.
- **Nome de Venda**: Implementação de validação personalizada para certificar-se de que o nome contém um espaço.

## Pipeline de Dados:

1. Os registros são lidos de uma lista.
2. Cada registro é validado contra a classe `SalesRecord`.
3. Registros validados são salvos em um arquivo CSV.

## Como executar:

1. Certifique-se de ter todas as bibliotecas necessárias instaladas.
2. Execute o script.
3. Verifique os registros validados no arquivo `sales_records.csv`.

## Dependências:

- `pydantic`
- `pandas`

## Contribuição

Fique à vontade para clonar, modificar e enviar pull requests. Toda contribuição é bem-vinda!

## Licença

MIT

---

Desenvolvido com 💙 por Luciano