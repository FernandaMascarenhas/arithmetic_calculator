"""Unit tests for the ArithmeticCalculator domain class."""

import unittest

from domain.calculator import ArithmeticCalculator


class TestArithmeticCalculator(unittest.TestCase):
    """Test suite covering arithmetic operations and domain boundary cases."""

    def setUp(self) -> None:
        """Instantiate the calculator before running each test method."""
        self.calculator: ArithmeticCalculator = ArithmeticCalculator()

    # -------------------------------------------------------------------------
    # Addition Tests
    # -------------------------------------------------------------------------

    def test_add_positive_numbers(self) -> None:
        """Ensure addition produces correct results with positive numbers."""
        first_operand: float = 15.0
        second_operand: float = 25.0
        expected_result: float = 40.0

        actual_result: float = self.calculator.add(first_operand, second_operand)

        self.assertEqual(actual_result, expected_result)

    def test_add_negative_numbers(self) -> None:
        """Ensure addition produces correct results with negative numbers."""
        first_operand: float = -10.0
        second_operand: float = -5.0
        expected_result: float = -15.0

        actual_result: float = self.calculator.add(first_operand, second_operand)

        self.assertEqual(actual_result, expected_result)

    def test_add_decimal_numbers(self) -> None:
        """Ensure addition handles floating-point precision correctly."""
        first_operand: float = 0.1
        second_operand: float = 0.2
        expected_result: float = 0.3

        actual_result: float = self.calculator.add(first_operand, second_operand)

        self.assertAlmostEqual(actual_result, expected_result, places=7)

    # -------------------------------------------------------------------------
    # Subtraction Tests
    # -------------------------------------------------------------------------

    def test_subtract_positive_numbers(self) -> None:
        """Ensure subtraction produces correct results with positive numbers."""
        first_operand: float = 50.0
        second_operand: float = 20.0
        expected_result: float = 30.0

        actual_result: float = self.calculator.subtract(first_operand, second_operand)

        self.assertEqual(actual_result, expected_result)

    def test_subtract_negative_numbers(self) -> None:
        """Ensure subtraction handles negative numbers correctly."""
        first_operand: float = -20.0
        second_operand: float = -30.0
        expected_result: float = 10.0

        actual_result: float = self.calculator.subtract(first_operand, second_operand)

        self.assertEqual(actual_result, expected_result)

    def test_subtract_decimal_numbers(self) -> None:
        """Ensure subtraction produces accurate floating-point results."""
        first_operand: float = 5.75
        second_operand: float = 2.25
        expected_result: float = 3.5

        actual_result: float = self.calculator.subtract(first_operand, second_operand)

        self.assertAlmostEqual(actual_result, expected_result, places=7)

    # -------------------------------------------------------------------------
    # Multiplication Tests
    # -------------------------------------------------------------------------

    def test_multiply_positive_numbers(self) -> None:
        """Ensure multiplication produces correct results with positive numbers."""
        first_operand: float = 6.0
        second_operand: float = 7.0
        expected_result: float = 42.0

        actual_result: float = self.calculator.multiply(first_operand, second_operand)

        self.assertEqual(actual_result, expected_result)

    def test_multiply_negative_numbers(self) -> None:
        """Ensure multiplication produces positive result when multiplying two negatives."""
        first_operand: float = -4.0
        second_operand: float = -3.0
        expected_result: float = 12.0

        actual_result: float = self.calculator.multiply(first_operand, second_operand)

        self.assertEqual(actual_result, expected_result)

    def test_multiply_decimal_numbers(self) -> None:
        """Ensure multiplication handles decimal values correctly."""
        first_operand: float = 2.5
        second_operand: float = 1.5
        expected_result: float = 3.75

        actual_result: float = self.calculator.multiply(first_operand, second_operand)

        self.assertAlmostEqual(actual_result, expected_result, places=7)

    # -------------------------------------------------------------------------
    # Division Tests
    # -------------------------------------------------------------------------

    def test_divide_positive_numbers(self) -> None:
        """Ensure division produces correct quotient with positive numbers."""
        dividend: float = 100.0
        divisor: float = 4.0
        expected_result: float = 25.0

        actual_result: float = self.calculator.divide(dividend, divisor)

        self.assertEqual(actual_result, expected_result)

    def test_divide_negative_numbers(self) -> None:
        """Ensure division handles negative operands correctly."""
        dividend: float = -50.0
        divisor: float = 2.0
        expected_result: float = -25.0

        actual_result: float = self.calculator.divide(dividend, divisor)

        self.assertEqual(actual_result, expected_result)

    def test_divide_decimal_numbers(self) -> None:
        """Ensure division handles decimal dividends and divisors."""
        dividend: float = 7.5
        divisor: float = 2.5
        expected_result: float = 3.0

        actual_result: float = self.calculator.divide(dividend, divisor)

        self.assertAlmostEqual(actual_result, expected_result, places=7)

    def test_divide_by_zero_raises_exception(self) -> None:
        """Verify that division by zero raises ZeroDivisionError with appropriate message."""
        dividend: float = 10.0
        divisor: float = 0.0

        with self.assertRaises(ZeroDivisionError) as error_context:
            self.calculator.divide(dividend, divisor)

        self.assertEqual(
            str(error_context.exception), "Division by zero is not allowed."
        )


if __name__ == "__main__":
    unittest.main()
