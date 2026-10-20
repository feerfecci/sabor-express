# sabor-express
Projeto desenvolvido junto ao curso de Python aplicando a Orientação a Objetos, da Alura, colocando em prática conceitos fundamentais de POO. A aplicação permite cadastrar restaurantes, gerenciar seu status de funcionamento e registrar avaliações, calculando a média das notas recebidas.  


Sabor Express — Gerenciamento de Restaurantes com Python
Projeto desenvolvido durante o curso de Orientação a Objetos com Python da Alura, com o objetivo de aplicar os principais conceitos de Programação Orientada a Objetos (POO) na construção de uma aplicação para gerenciamento de restaurantes e avaliações.

Sobre o Projeto
O Sabor Express permite representar restaurantes por meio de classes em Python, acompanhar seu status de funcionamento e registrar avaliações realizadas por clientes.

A aplicação utiliza uma estrutura modular, separando a regra de negócio dos restaurantes da implementação das avaliações para garantir manutenibilidade e boa organização do código.

Funcionalidades
Cadastro de restaurantes: registro por nome e categoria.

Listagem de estabelecimentos: exibição dos restaurantes cadastrados no sistema.

Gestão de status: ativação e desativação do funcionamento de restaurantes.

Registro de avaliações: inclusão de notas e comentários de clientes com validação.

Métricas: cálculo automatizado da média de avaliações por restaurante.

Tecnologias Utilizadas
Linguagem: Python 3

Paradigma: Programação Orientada a Objetos (POO)

Versionamento: Git e GitHub

Conceitos Praticados
Durante o desenvolvimento, foram aplicados os seguintes fundamentos de POO e engenharia de software:

Classes e Objetos: abstração do domínio de restaurantes e avaliações.

Método Construtor (__init__): inicialização dos atributos dos objetos.

Encapsulamento: proteção de atributos com convenção de acesso privado/protegido (_nome, _ativo, _avaliacoes).

Métodos de Instância: implementação das regras de negócio de cada restaurante.

Propriedades (@property): controle de acesso e formatação para o status e média de notas.

Métodos de Classe (@classmethod): manipulação e consulta global dos restaurantes da classe.

Composição: associação entre a classe restaurante e suas respectivas avaliações.

Modularização: separação de responsabilidades em arquivos e pacotes distintos.

Estrutura do Projeto
Plaintext
sabor-express/
├── models/
│   ├── __init__.py
│   ├── restaurant.py
│   └── evaluation.py
├── app.py
└── README.md
Nota: Ajuste os nomes de diretórios e arquivos conforme a estrutura exata do seu repositório.

Como Executar
Pré-requisitos
Python 3 instalado na máquina.

Git (opcional, para clonagem).

Instruções
Clone o repositório:

Bash
git clone URL_DO_REPOSITORIO
Acesse a pasta do projeto:

Bash
cd sabor-express
Execute a aplicação:

Bash
python app.py
No Windows, você também pode usar py app.py.

Exemplo de Uso
Exemplo de instanciação de restaurantes e registro de avaliações no código:

Python
from models.restaurant import Restaurant

# Criando uma nova instância
restaurante_praca = Restaurant("Praça", "Gourmet")

# Registrando avaliações
restaurante_praca.receive_evaluation("Gui", 5)
restaurante_praca.receive_evaluation("Fe", 4)

# Alterando o status de funcionamento
restaurante_praca.toggle_status()

# Exibindo a lista consolidada
Restaurant.list_restaurants()
Objetivo do Projeto
Este repositório consolida o aprendizado prático da sintaxe e dos pilares de Programação Orientada a Objetos em Python, focando na escrita de código limpo, reutilizável e coeso.

Status: Projeto finalizado (Curso de POO — Alura)
