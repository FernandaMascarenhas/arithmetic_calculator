"""Application entry point for the arithmetic calculator."""

from domain.calculator import ArithmeticCalculator
from user_interface.console_interface import ConsoleUserInterface


def main() -> None:
    """Instantiate application components and start the execution loop."""
    calculator: ArithmeticCalculator = ArithmeticCalculator()
    user_interface: ConsoleUserInterface = ConsoleUserInterface(calculator)
    user_interface.run_application_loop()


if __name__ == "__main__":
    main()
