# Sabor Express — Gerenciamento de Restaurantes com Python
Projeto desenvolvido junto ao curso de Python aplicando a Orientação a Objetos, da Alura, colocando em prática conceitos fundamentais de POO. A aplicação permite cadastrar restaurantes, gerenciar seu status de funcionamento e registrar avaliações, calculando a média das notas recebidas.

## Sobre o Projeto

O **Sabor Express** permite cadastrar restaurantes, acompanhar seu status de funcionamento e registrar avaliações de clientes, calculando automaticamente a média das notas recebidas.

A aplicação utiliza uma estrutura modular, separando as classes de restaurantes e avaliações para favorecer a organização, a reutilização e a manutenção do código.

## Funcionalidades

- **Cadastro de restaurantes:** registro por nome e categoria.
- **Listagem de restaurantes:** exibição dos estabelecimentos, suas categorias, médias de avaliações e status.
- **Gestão de status:** ativação e desativação do funcionamento dos restaurantes.
- **Registro de avaliações:** inclusão de notas atribuídas por clientes, com validação dos valores permitidos.
- **Cálculo de médias:** cálculo automático da média das avaliações de cada restaurante.

## Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Versionamento:** Git e GitHub

## Conceitos Praticados

Durante o desenvolvimento, foram aplicados os seguintes conceitos:

- **Classes e Objetos:** representação dos restaurantes e das avaliações.
- **Método Construtor (`__init__`):** inicialização dos atributos dos objetos.
- **Encapsulamento:** utilização de atributos com convenção de acesso não público, como `_name`, `_active` e `_evaluations`.
- **Métodos de Instância:** implementação dos comportamentos e das regras de negócio dos restaurantes.
- **Propriedades (`@property`):** acesso ao status de funcionamento e à média das avaliações.
- **Métodos de Classe (`@classmethod`):** listagem dos restaurantes cadastrados na classe.
- **Composição:** associação entre restaurantes e suas respectivas avaliações.
- **Modularização:** separação das classes em arquivos distintos.

## Estrutura do Projeto

```text
sabor-express/
├── models/
│   ├── __init__.py
│   ├── restaurant.py
│   └── avaluation.py
├── app.py
└── README.md
```

> **Nota:** A estrutura acima é ilustrativa. Ajuste os nomes dos arquivos conforme a estrutura real do repositório. No código atual, o módulo de avaliações utiliza o nome `avaluation.py`.

## Como Executar

### Pré-requisitos

- Python 3 instalado na máquina.
- Git instalado, caso deseje clonar o repositório.

### Instruções

1. Clone o repositório:

   ```bash
   git clone URL_DO_REPOSITORIO
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd sabor-express
   ```

3. Execute a aplicação:

   ```bash
   python app.py
   ```

   No Windows, também é possível utilizar:

   ```bash
   py app.py
   ```

> **Importante:** Substitua `URL_DO_REPOSITORIO` pelo endereço real do repositório e utilize o nome correto do arquivo principal.

## Exemplo de Uso

Exemplo de criação de restaurantes, registro de avaliações e alteração do status de funcionamento:

```python
from models.restaurant import Restaurant

# Criando um restaurante
restaurante_praca = Restaurant("Praça", "Gourmet")

# Registrando avaliações
restaurante_praca.get_avaluation("Gui", 5)
restaurante_praca.get_avaluation("Fe", 4)

# Alterando o status de funcionamento
restaurante_praca.update_status()

# Listando os restaurantes cadastrados
Restaurant.list_restaurants()
```

## Objetivo do Projeto

Este projeto consolida o aprendizado prático de Programação Orientada a Objetos em Python, com foco na organização do código, na separação de responsabilidades e na construção de uma aplicação baseada em classes e objetos.

**Status:** Projeto de aprendizado desenvolvido durante o curso de Orientação a Objetos com Python da Alura.
