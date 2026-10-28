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

Saída: `domain/calculator.py`

## Análise Conceitual e Casos de Borda

### Prompt enviado
```
Gostei da implementação de ArithmeticCalculator, mas quero aprofundar nos comportamentos em tempo de execução e entender possíveis vulnerabilidades antes de avançarmos.

Poderia me explicar, de forma didática e conceitual:
1. O que acontece internamente se chamarmos os métodos passando strings numéricas (ex.: "10") ou strings alfanuméricas inválidas (ex.: "2f57r")? Como o Python reage a isso em tempo de execução, considerando que usamos type hints?
2. Em termos de design de software (separação de responsabilidades), faz mais sentido blindar a classe de domínio contra esses valores inválidos ou delegar toda a validação e conversão de tipos para a camada de interface?
3. Além da divisão por zero, existem outros casos de borda matemáticos ou limitações do tipo float no Python (como NaN, infinitos ou estouro de precisão) que valeria a pena tratar aqui?

Por favor, foque na explicação conceitual e nos prós e contras de cada abordagem, sem gerar código de refatoração por enquanto.
```

### Decisões de Design Registradas
1. **Fronteira de Validação (Clean Architecture):**
   * O domínio (`ArithmeticCalculator`) mantém foco exclusivo no cálculo puro e no disparo de `ZeroDivisionError`.
   * A camada de interface (`ConsoleUserInterface`) será a barreira de entrada responsável por sanitização, parsing (`float`) e captura de `ValueError`.
2. **Tratamento de Strings em Runtime:**
   * Type hints não validam tipos em execução; passar strings para `add` causaria concatenação acidental, reforçando a necessidade de validação na interface.
3. **Ponto Flutuante (IEEE 754):**
   * O uso de `float` é mantido para fins didáticos, ciente das limitações de precisão binária.
   * A interface deve barrar strings literais como `"nan"`, `"inf"` e `"-inf"`, impedindo estados matemáticos indeterminados no domínio.

## Prompt para geração da interface

```
Agora quero implementar a camada de interface de console ('user_interface/console_interface.py').

A aplicação deve permitir que o usuário:
- Veja um menu com as 4 operações básicas e uma opção de sair.
- Escolha uma operação e digite os dois valores para o cálculo.
- Veja o resultado formatado de forma clara.
- Seja avisado caso digite valores inválidos (letras ou entradas que não façam sentido), sem que o programa trave.
- Receba uma mensagem clara caso tente fazer uma divisão por zero.
- Continue usando a calculadora até escolher explicitamente a opção de sair.

Requisitos técnicos:
- Utilize a classe ArithmeticCalculator implementada anteriormente para fazer os cálculos.
- Aplique as decisões de validação e sanitização que discutimos na etapa anterior.
- Mantenha o código limpo, em inglês, com type hints e seguindo a PEP 8.

Por favor, gere a implementação de 'console_interface.py' e explique brevemente como a interface se conecta à calculadora.
```

Saída: `user_interface/console_interface.py`

### Como a Interface se Conecta à Calculadora

A comunicação entre a camada de apresentação e a camada de domínio ocorre por meio de **Injeção de Dependência via construtor**:

1. **Desacoplamento:** A classe `ConsoleUserInterface` não instancia `ArithmeticCalculator` internamente com `ArithmeticCalculator()`. Em vez disso, ela recebe uma instância pronta através do método `__init__(self, calculator: ArithmeticCalculator)`.
2. **Fronteira Clara de Responsabilidades:** 
   * A interface cuida de todo o atrito com o mundo externo: lê o teclado, rejeita strings literais perigosas (`nan`, `inf`), captura `ValueError` repetindo a pergunta e traduz a opção escolhida.
   * Quando os dados chegam à `self.calculator`, eles já são números válidos (`float`).
3. **Resiliência a Falhas do Domínio:** Ao chamar `self.calculator.divide(...)`, a interface envolve a execução em um bloco `try...except ZeroDivisionError`. Isso intercepta a exceção levantada pelo domínio e a converte em uma mensagem amigável no console, impedindo a quebra do programa e permitindo que o loop continue normalmente.

### Prompt de revisão

```
Gostei da implementação de ConsoleUserInterface, mas analisando o método execute_operation, notei que as linhas que solicitam os operandos com read_numeric_input se repetem de forma quase idêntica em todas as opções (1 a 4).

Pensando em boas práticas de Clean Code e no princípio DRY (Don't Repeat Yourself):
1. Como podemos refatorar o método execute_operation para eliminar essa duplicação na leitura dos operandos?
2. Quais são as abordagens idiomáticas em Python moderno (por exemplo, uso de dicionários mapeando operações, match/case ou separação de responsabilidades na coleta dos dados)?
3. Apresente a versão refatorada apenas do método execute_operation (ou da classe, se julgar necessário) explicando as vantagens da abordagem escolhida.
```

Adição de método `read_operands` e modificação de `execute_operation`.

## Prompt para criação da `main.py`

```
Agora que temos a calculadora e a interface de console prontas, precisamos do arquivo de inicialização 'main.py' para rodar o projeto.

Crie o arquivo de inicialização conectando os componentes existentes e iniciando o loop da aplicação.
```

Saída: `main.py`
