"""User interface module providing terminal interactions for the calculator."""

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
        print("5. Exit application")
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

    def execute_operation(self, selected_option: str) -> None:
        """Gather operands, perform the calculation, and display results.

        Parameters:
            selected_option: The string identifier of the chosen menu option.
        """
        if selected_option == "1":
            first_operand: float = self.read_numeric_input("Enter the first operand: ")
            second_operand: float = self.read_numeric_input("Enter the second operand: ")
            result: float = self.calculator.add(first_operand, second_operand)
            print(f"Result: {first_operand} + {second_operand} = {result}")

        elif selected_option == "2":
            first_operand: float = self.read_numeric_input("Enter the first operand: ")
            second_operand: float = self.read_numeric_input("Enter the second operand: ")
            result: float = self.calculator.subtract(first_operand, second_operand)
            print(f"Result: {first_operand} - {second_operand} = {result}")

        elif selected_option == "3":
            first_operand: float = self.read_numeric_input("Enter the first operand: ")
            second_operand: float = self.read_numeric_input("Enter the second operand: ")
            result: float = self.calculator.multiply(first_operand, second_operand)
            print(f"Result: {first_operand} * {second_operand} = {result}")

        elif selected_option == "4":
            dividend: float = self.read_numeric_input("Enter the dividend: ")
            divisor: float = self.read_numeric_input("Enter the divisor: ")
            try:
                result: float = self.calculator.divide(dividend, divisor)
                print(f"Result: {dividend} / {divisor} = {result}")
            except ZeroDivisionError as error:
                print(f"Calculation Error: {error}")

    def run_application_loop(self) -> None:
        """Execute the primary interaction loop until the user exits."""
        valid_options: set[str] = {"1", "2", "3", "4", "5"}

        while True:
            self.display_menu()
            selected_option: str = input("Please select an option (1-5): ").strip()

            if selected_option not in valid_options:
                print("Error: Unrecognized option. Please choose a number between 1 and 5.")
                continue

            if selected_option == "5":
                print("Exiting application. Goodbye!")
                break

            self.execute_operation(selected_option)
