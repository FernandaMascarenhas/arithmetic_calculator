# Console Arithmetic Calculator

A clean, modular, and fully object-oriented arithmetic calculator developed in Python. This project follows strict PEP 8 guidelines, uses comprehensive static typing (*type hints*), and completely eliminates abbreviations and contractions across all identifiers, packages, and modules.

---

## Architectural Principles

The application is structured according to fundamental Clean Architecture and software engineering principles:

1. **Separation of Concerns (Domain versus User Interface):**
   * **Domain Layer (`domain/calculator.py`):** The `ArithmeticCalculator` class is an isolated engine responsible purely for mathematical calculations. It has zero knowledge of the terminal, user inputs, or output formatting. It enforces arithmetic invariants (such as preventing division by zero).
   * **Presentation Layer (`user_interface/console_interface.py`):** The `ConsoleUserInterface` class handles all input and output operations, menu rendering, input parsing, and graceful error presentation.

2. **Dependency Injection:**
   * The `ConsoleUserInterface` does not instantiate the calculator internally. Instead, an instance of `ArithmeticCalculator` is injected through its constructor. This design enables high modularity and straightforward testing.

3. **DRY Principle via Dispatch Table:**
   * The application avoids duplicated operand prompt logic by centralizing binary operand retrieval into a single method (`read_operands`).
   * Operations are managed via an in-memory dispatch table mapping choices to callable functions (`Callable[[float, float], float]`) and mathematical symbols. This adheres to the Open/Closed Principle (OCP), making it easy to introduce new operations without altering execution flow.

4. **Input Sanitization and Fault Tolerance:**
   * User inputs are strictly validated before reaching the domain layer.
   * Floating-point edge cases (such as `"nan"`, `"inf"`, and `"-inf"`) are explicitly intercepted and rejected at the boundary layer.
   * Non-numeric strings raise handled `ValueError` exceptions without terminating the program.

---

## Directory Structure

```text
arithmetic_calculator/
│
├── documentation/
│   ├── architectural_plan.md
│   ├── execution_log.md
│   └── lesson_01_reference.docx
│
├── domain/
│   ├── __init__.py
│   └── calculator.py             # Core mathematical logic (ArithmeticCalculator)
│
├── user_interface/
│   ├── __init__.py
│   └── console_interface.py      # Console presentation layer (ConsoleUserInterface)
│
├── tests/
│   ├── __init__.py
│   └── test_calculator.py        # Automated test suite using unittest
│
├── .gitignore                    # Version control ignore specifications
├── main.py                       # Application bootstrap and entry point
└── README.md                     # Project documentation
```

---

## Requirements

* **Python 3.10** or higher (uses native collection type hints such as `tuple[float, float]` and `collections.abc.Callable`).

---

## How to Run the Application

Execute the entry point from the root directory of the repository:

```bash
python main.py
```

---

## How to Run Automated Unit Tests

The test suite is built on Python's standard `unittest` framework and comprises **16 unit tests** covering addition, subtraction, multiplication, division, and percentage calculations across positive numbers, negative numbers, floating-point precision (via `assertAlmostEqual`), and exception raising on division by zero.

Run all tests with detailed verbosity from the project root:

```bash
python -m unittest --verbose
```

Alternatively, run the test module directly:

```bash
python -m unittest tests/test_calculator.py
```

---

## Conceptual Architecture Q&A

### 1. What are the primary components and their responsibilities?
* **`ArithmeticCalculator` (Domain):** Encapsulates binary mathematical logic (`add`, `subtract`, `multiply`, `divide`, `calculate_percentage`). It produces numerical outputs or raises domain exceptions (`ZeroDivisionError`).
* **`ConsoleUserInterface` (User Interface):** Manages the terminal user lifecycle: displaying options, collecting string inputs, converting strings to floats, invoking the appropriate domain method, and printing formatted results.
* **`main.py` (Composition Root):** Instantiates the dependencies, wires them together, and triggers the main application loop.

### 2. How are user inputs received and validated?
All terminal interactions pass through `ConsoleUserInterface.read_numeric_input`:
1. The method prompts the user and removes leading/trailing whitespace.
2. It verifies that the input is not a reserved floating-point literal (`"nan"`, `"inf"`, `"-inf"`).
3. It attempts to parse the string to a `float`. If conversion fails with a `ValueError`, an error message is displayed, and the prompt repeats until a valid number is provided.
4. Cleaned `float` values are then provided to the `ArithmeticCalculator`.

### 3. What is the execution flow of an operation?
1. The user starts the application via `main.py`.
2. `ConsoleUserInterface.run_application_loop` renders the main menu.
3. The user selects an option (`1` through `6`).
4. If an arithmetic option (`1` to `5`) is chosen:
   * The program retrieves the corresponding callable method and symbol from the dispatch table.
   * `read_operands` requests the two required numbers from the user.
   * The selected method on `ArithmeticCalculator` is invoked inside a `try...except ZeroDivisionError` block.
   * The formatted equation and result are displayed on the terminal.
5. The menu reappears until option `6` (Exit application) is selected.
