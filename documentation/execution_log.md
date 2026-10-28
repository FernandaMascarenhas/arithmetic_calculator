# Desafio 1 - Calculadora Simples Python

**Modelo**: gemini-3.8-flash

## System Instructions

```text
Você é um mentor especialista em Engenharia de Software e Python. Seu objetivo é ajudar no desenvolvimento de código limpo, modular e didático. Sempre utilize boas práticas (PEP 8, tipagem estática com type hints e tratamento adequado de erros). Ao explicar o código, seja direto, conceitual e estruture as respostas com clareza técnica.
```

---

## Passo 1: Planejamento Arquitetural

### Prompt Inicial

```text
Quero desenvolver uma calculadora em Python que realize as quatro operações básicas. Antes de escrever qualquer linha de código, quero estruturar o projeto.

Me ajude a planejar a arquitetura da aplicação:
1. Sugestões de nomes para o projeto.
2. Modelagem básica em Orientação a Objetos (quais classes seriam necessárias e quais as responsabilidades de cada uma, separando a lógica matemática da interface de console).
3. Assinatura dos métodos previstos e tratamento de casos excepcionais (como divisão por zero).

Não gere a implementação completa do código agora; foque na estrutura conceitual e nas decisões de design.
```

### Segundo Prompt: Eliminação de Abreviações e Conformidade PEP 8

```text
Gostei da divisão de responsabilidades, mas não quero abreviações em nenhum ponto do projeto. Quero que todo o projeto seja padronizado em inglês, seguindo rigorosamente a PEP 8 (snake_case para pacotes, módulos, funções e métodos; PascalCase para classes).

Por favor, faça apenas o seguinte:
1. Sugira novos nomes para o projeto que sejam consistentes, descritivos e sem contrações/siglas.
2. Ajuste o plano arquitetural e a árvore de diretórios substituindo qualquer termo abreviado (por exemplo, nada de 'calc', 'cli' ou 'ui') por termos completos e autoexplicativos em inglês.

Não escreva o código ainda.
```

**Saída gerada:** `documentation/architectural_plan.md`

---

## Passo 2: Camada de Domínio (`ArithmeticCalculator`)

### Prompt Enviado

```text
Gere apenas a implementação do módulo da camada de domínio ('domain/calculator.py'), contendo:

- Tipagem estática estrita (type hints).
- Docstrings curtas em inglês para a classe e seus métodos.
- Tratamento explícito de erros.

Não implemente a interface de terminal ainda.
```

**Saída gerada:** `domain/calculator.py`

---

## Passo 3: Análise Conceitual e Casos de Borda

### Prompt Enviado

```text
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



---

## Passo 4: Camada de Interface (`ConsoleUserInterface`)

### Prompt Enviado

```text
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

### Como a Interface se Conecta à Calculadora

1. **Desacoplamento:** A classe `ConsoleUserInterface` recebe uma instância de `ArithmeticCalculator` via construtor (`__init__`), aplicando injeção de dependência.
2. **Fronteira Clara de Responsabilidades:** A interface cuida do atrito com o console: sanitiza o input, rejeita literais perigosos (`nan`, `inf`), captura `ValueError` repetindo a pergunta e converte dados para `float`.
3. **Resiliência a Falhas do Domínio:** A invocação das operações é protegida por um bloco `try...except ZeroDivisionError`, convertendo a exceção matemática em mensagem amigável sem quebrar o loop.

---

## Passo 5: Refatoração DRY e Dispatch Table

### Prompt de Revisão

```text
Gostei da implementação de ConsoleUserInterface, mas analisando o método execute_operation, notei que as linhas que solicitam os operandos com read_numeric_input se repetem de forma quase idêntica em todas as opções (1 a 4).

Pensando em boas práticas de Clean Code e no princípio DRY (Don't Repeat Yourself):
1. Como podemos refatorar o método execute_operation para eliminar essa duplicação na leitura dos operandos?
2. Quais são as abordagens idiomáticas em Python moderno (por exemplo, uso de dicionários mapeando operações, match/case ou separação de responsabilidades na coleta dos dados)?
3. Apresente a versão refatorada apenas do método execute_operation (ou da classe, se julgar necessário) explicando as vantagens da abordagem escolhida.
```

### Decisões da Refatoração

* **Método `read_operands`:** Centraliza a leitura sanitizada dos dois operandos binários em uma tupla `tuple[float, float]`.
* **Tabela de Despacho (*Dispatch Table*):** Dicionário mapeando a opção para uma tupla `tuple[Callable[[float, float], float], str]`, eliminando blocos `if/elif` repetitivos e aderindo ao Open/Closed Principle (OCP).

**Saída gerada:** `user_interface/console_interface.py` (atualizado)

---

## Passo 6: Bootstrap da Aplicação (`main.py`)

### Prompt Enviado

```text
Agora que temos a calculadora e a interface de console prontas, precisamos do arquivo de inicialização 'main.py' para rodar o projeto.

Crie o arquivo de inicialização conectando os componentes existentes e iniciando o loop da aplicação.
```

**Saída gerada:** `main.py`

---

## Passo 7: Camada de Testes Automatizados

### Prompt Enviado

```text
Agora que a camada de domínio ('domain/calculator.py') e a interface estão prontas, quero adicionar uma camada de testes unitários para validar as operações da calculadora.

Por favor, faça o seguinte:
1. Sugira onde posicionar a pasta de testes na estrutura de diretórios do projeto seguindo as boas práticas em Python.
2. Gere a implementação do arquivo de testes unitários utilizando o framework nativo 'unittest'.
3. Cubra as 4 operações básicas com números positivos, negativos, decimais e o caso de exceção de divisão por zero.
4. Mantenha os testes limpos, em inglês, com asserções explícitas e nomes de métodos descritivos.
5. Mostre o comando de terminal para executar todos os testes.
```

**Saída gerada:** `tests/test_calculator.py`

---

## Passo 8: Configuração do Git e Documentação Final

### Prompt Enviado

```text
Para finalizar o projeto e prepará-lo para publicação no GitHub, preciso de dois arquivos de configuração e documentação:

1. Um arquivo '.gitignore' configurado para projetos Python (ignorando __pycache__, arquivos de ambiente virtual, lixo de sistema operacional e IDEs).
2. O arquivo 'README.md' completo do repositório, em inglês, contendo:
   - Título e visão geral do projeto.
   - Os princípios arquiteturais adotados (separação entre domínio e interface, uso de tabela de despacho/DRY e sanitização de entradas).
   - A árvore final de diretórios do projeto (incluindo a pasta de testes e documentação).
   - Instruções de como rodar a aplicação e como executar os testes automatizados com unittest.
   - Tópico com as respostas conceituais para as perguntas do desafio (componentes principais, recebimento de dados e fluxo de execução).

Gere o conteúdo pronto para ser salvo nesses dois arquivos.
```

**Saídas geradas:** `.gitignore` e `README.md`

---

## Validação e Execução

### Testes Manuais de Terminal (`python3 main.py`)

* [x] Sanitização de entradas com caracteres inválidos, aspas e alfanuméricos (repetição da solicitação com tratamento de `ValueError`).
* [x] Bloqueio de literais especiais de ponto flutuante (`nan`, `inf`).
* [x] Execução correta das quatro operações binárias com inteiros e números de ponto flutuante.
* [x] Captura amigável de `ZeroDivisionError` sem interrupção do processo.
* [x] Encerramento correto da aplicação com a opção 5.

### Testes Automatizados (`python3 -m unittest --verbose`)

* [x] 13 testes unitários cobrindo adição, subtração, multiplicação e divisão com números positivos, negativos e decimais (`assertAlmostEqual`).
* [x] Validação de disparo e mensagem de exceção para divisão por zero (`assertRaises(ZeroDivisionError)`).
