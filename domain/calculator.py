"""Domain module responsible for fundamental arithmetic calculations."""


class ArithmeticCalculator:
    """Provides methods to perform basic mathematical operations."""

    def add(self, first_operand: float, second_operand: float) -> float:
        """Calculate the sum of two operands."""
        return first_operand + second_operand

    def subtract(self, first_operand: float, second_operand: float) -> float:
        """Subtract the second operand from the first operand."""
        return first_operand - second_operand

    def multiply(self, first_operand: float, second_operand: float) -> float:
        """Calculate the product of two operands."""
        return first_operand * second_operand

    def divide(self, dividend: float, divisor: float) -> float:
        """Divide the dividend by the divisor.

        Raises:
            ZeroDivisionError: If the divisor is equal to zero.
        """
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        return dividend / divisor
