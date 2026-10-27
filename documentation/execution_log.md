# Desafio 1 - Calculadora Simples Python

**Modelo**: gemini-3.8-flash

## System instructions

```
Você é um mentor especialista em Engenharia de Software e Python. Seu objetivo é ajudar no desenvolvimento de código limpo, modular e didático. Sempre utilize boas práticas (PEP 8, tipagem estática com type hints e tratamento adequado de erros). Ao explicar o código, seja direto, conceitual e estruture as respostas com clareza técnica.
```

## Passo 1: Playground

### Prompt inicial

```
Quero desenvolver uma calculadora em Python que realize as quatro operações básicas. Antes de escrever qualquer linha de código, quero estruturar o projeto.

Me ajude a planejar a arquitetura da aplicação:
1. Sugestões de nomes para o projeto.
2. Modelagem básica em Orientação a Objetos (quais classes seriam necessárias e quais as responsabilidades de cada uma, separando a lógica matemática da interface de console).
3. Assinatura dos métodos previstos e tratamento de casos excepcionais (como divisão por zero).

Não gere a implementação completa do código agora; foque na estrutura conceitual e nas decisões de design.
```

### Segundo prompt

```
Gostei da divisão de responsabilidades, mas não quero abreviações em nenhum ponto do projeto. Quero que todo o projeto seja padronizado em inglês, seguindo rigorosamente a PEP 8 (snake_case para pacotes, módulos, funções e métodos; PascalCase para classes).

Por favor, faça apenas o seguinte:
1. Sugira novos nomes para o projeto que sejam consistentes, descritivos e sem contrações/siglas.
2. Ajuste o plano arquitetural e a árvore de diretórios substituindo qualquer termo abreviado (por exemplo, nada de 'calc', 'cli' ou 'ui') por termos completos e autoexplicativos em inglês.

Não escreva o código ainda.
```

Saída do plano inicial: `arithmetic_calculator/plan.md`

## Prompt para geração da camada de domínio

```
Gere apenas a implementação do módulo da camada de domínio ('domain/calculator.py'), contendo:

- Tipagem estática estrita (type hints).
- Docstrings curtas em inglês para a classe e seus métodos.
- Tratamento explícito de erros.

Não implemente a interface de terminal ainda. 
```