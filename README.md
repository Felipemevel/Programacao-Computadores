#  IFRN Codeforces Solutions: Python

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![IFRN](https://img.shields.io/badge/Instituicao-IFRN-32CD32?style=for-the-badge&logo=readthedocs&logoColor=white)
![Codeforces](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightyellow?style=for-the-badge&logo=git&logoColor=white)

> **Portfólio acadêmico de evolução na disciplina de Programação de Computadores | TADS - IFRN**

---

## Sobre o Projeto

Este repositório documenta a minha jornada completa de aprendizado em **Lógica de Programação e Algoritmos** utilizando **Python**. As soluções aqui presentes resolvem problemas propostos no ambiente **Codeforces** (adaptado para o IFRN), organizados em 10 listas que cobrem desde a introdução à sintaxe até a resolução de problemas complexos integrados.

O objetivo é demonstrar a aplicação prática de conceitos de Engenharia de Software, como **Clean Code**, **Modularização** e domínio da sintaxe Pythonica.

---

## Evolução do Aprendizado (Roadmap)

Cada lista representa um degrau na complexidade lógica e sintática. Abaixo, o mapeamento das competências desenvolvidas:

| Diretório | Foco do Aprendizado | Conceitos Chave Aplicados |
| :--- | :--- | :--- |
| **📂 Lista01** | **Fundamentos & I/O** | Entrada/Saída de dados, tipagem forte (`int`, `float`, `str`) e operadores aritméticos básicos. |
| **📂 Lista02** | **Formatação de Dados** | Manipulação de strings, precisão decimal (`.2f`), f-strings e apresentação de dados. |
| **📂 Lista03** | **Condicionais Básicas** | Introdução à tomada de decisão (`if/else`) e lógica booleana simples. |
| **📂 Lista04** | **Lógica Condicional II** | Aprofundamento em decisões, operadores relacionais e resolução de problemas matemáticos condicionais. |
| **📂 Lista05** | **Condicionais Avançadas** | Estruturas aninhadas (`elif`), validação de dados complexos e otimização de fluxos de decisão. |
| **📂 Lista06** | **Modularização (Funções)** | Criação de funções (`def`), escopo de variáveis, parâmetros, retorno e encapsulamento de lógica. |
| **📂 Lista07** | **Laços de Repetição (For)** | Iteração definida (`range`), percurso de sequências e automação de tarefas repetitivas. |
| **📂 Lista08** | **Laços de Repetição (While)** | Iteração indefinida, loops condicionais, flags e controle de fluxo (`break`/`continue`). |
| **📂 Lista09** | **Laços Aprofundados** | Algoritmos complexos combinando `for` e `while`, loops aninhados e tratamento de exceções. |
| **📂 Lista10** | **Integração (Capstone)** | **Desafios Finais:** União de condicionais, laços, listas e lógica avançada para resolução de problemas reais. |

---

## Tecnologias & Ferramentas

* **Linguagem:** Python 3.12+
* **IDE:** Visual Studio Code (VS Code)
* **Formatação:** Black Formatter (PEP 8 Compliance)
* **Ambiente:** Linux (Fedora/Debian based)

---

## Estrutura do Repositório

A organização segue a cronologia da disciplina, facilitando a visualização do progresso:

```text
Codeforces/
│
├── 📁 Lista01/           # I/O e Operadores
│   ├── A-SomaSimples.py
│   └── ...
├── 📁 Lista02/           # Formatação
│   ├── C-SalarioBonus.py
│   └── ...
├── 📁 Lista03/           # Condicionais
│   ├── A-Iguais?.py
│   └── ...
├── 📁 Lista04/           # Condicionais II
│   ├── A-FrotaDeTaxi.py
│   └── ...
├── 📁 Lista05/           # Condicionais III
│   ├── A-Corrida.py
│   └── ...
├── 📁 Lista06/           # Funções
│   ├── A-SomaSimplesFunc.py
│   └── ...
├── 📁 Lista07/           # Laço For
│   ├── A-Tabuada.py
│   └── ...
├── 📁 Lista08/           # Laço While
│   ├── D-NumeroPrimo.py
│   └── ...
├── 📁 Lista09/           # Loops Avançados
│   ├── I-MacacoPrego.py
│   └── ...
├── 📁 Lista10/           # Integração Final
│   ├── A-Chinelos.py
│   └── ...
│
└── 📄 README.md
```
## Exemplo de código
Este exemplo foi feito utilizando o primeiro desafio da lista 10, aprimorado e implementando em uma função. 

```
def processar_pedidos(estoque: int, pedidos: int) -> int:

    entregues = 0

    for pedido in pedidos:
        tamanho_ajustado = pedido - 1  # Ajuste de índice

        if estoque[tamanho_ajustado] > 0:

            estoque[tamanho_ajustado] -= 1
            entregues += 1
            
    return entregues
```
