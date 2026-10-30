"""User interface module providing terminal interactions for the calculator."""
from collections.abc import Callable
from domain.calculator import ArithmeticCalculator


class ConsoleUserInterface:
    """Manages console interactions, input sanitization, and output formatting."""

    def __init__(self, calculator: ArithmeticCalculator) -> None:
        """Initialize the interface with a calculator instance.

        Parameters:
            calculator: An instance of ArithmeticCalculator used for computations.
        """
        self.calculator: ArithmeticCalculator = calculator

    def display_menu(self) -> None:
        """Display the available menu options to the user."""
        print("\n========================================")
        print("         ARITHMETIC CALCULATOR          ")
        print("========================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Exit application")
        print("========================================")

    def read_numeric_input(self, prompt_message: str) -> float:
        """Prompt the user for a numeric value and sanitize the input.

        Parameters:
            prompt_message: The text displayed when requesting input.

        Returns:
            A valid float representation of the entered number.
        """
        disallowed_literals: set[str] = {"nan", "inf", "-inf", "+inf"}

        while True:
            raw_input_value: str = input(prompt_message).strip()

            if raw_input_value.lower() in disallowed_literals:
                print("Error: Special floating-point literals are not permitted.")
                continue

            try:
                return float(raw_input_value)
            except ValueError:
                print("Error: Invalid numeric input. Please enter a valid number.")

    def read_operands(self) -> tuple[float, float]:
        """Prompt the user for both binary arithmetic operands.

        Returns:
            A tuple containing the first operand and the second operand.
        """
        first_operand: float = self.read_numeric_input("Enter the first operand: ")
        second_operand: float = self.read_numeric_input("Enter the second operand: ")
        return first_operand, second_operand

    def execute_operation(self, selected_option: str) -> None:
        """Execute the arithmetic calculation corresponding to the selected option.

        Parameters:
            selected_option: The string identifier of the chosen menu option.
        """
        operation_mappings: dict[str, tuple[Callable[[float, float], float], str]] = {
            "1": (self.calculator.add, "+"),
            "2": (self.calculator.subtract, "-"),
            "3": (self.calculator.multiply, "*"),
            "4": (self.calculator.divide, "/"),
            "5": (self.calculator.calculate_percentage, "%"),
        }

        operation_function, mathematical_symbol = operation_mappings[selected_option]

        first_operand, second_operand = self.read_operands()

        try:
            calculation_result: float = operation_function(first_operand, second_operand)
            print(
                f"Result: {first_operand} {mathematical_symbol} "
                f"{second_operand} = {calculation_result}"
            )
        except ZeroDivisionError as error:
            print(f"Calculation Error: {error}")

    def run_application_loop(self) -> None:
        """Execute the primary interaction loop until the user exits."""
        valid_options: set[str] = {"1", "2", "3", "4", "5", "6"}

        while True:
            self.display_menu()
            selected_option: str = input("Please select an option (1-6): ").strip()

            if selected_option not in valid_options:
                print("Error: Unrecognized option. Please choose a number between 1 and 6.")
                continue

            if selected_option == "6":
                print("Exiting application. Goodbye!")
                break

            self.execute_operation(selected_option)
