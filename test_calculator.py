"""
Unit tests for Python Tkinter Calculator expression logic.
"""
import unittest
import math

def calculate_expression(expr: str) -> str:
    """Safely evaluates an arithmetic expression."""
    try:
        # Prevent unsafe builtins
        allowed_names = {"__builtins__": None, "math": math, "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan}
        result = eval(expr, allowed_names, {})
        # Format floating numbers nicely
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)
    except ZeroDivisionError:
        return "Error: Div/0"
    except Exception:
        return "Error"

class TestCalculatorLogic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate_expression("12+34"), "46")
        self.assertEqual(calculate_expression("0.5+0.25"), "0.75")

    def test_subtraction(self):
        self.assertEqual(calculate_expression("100-45"), "55")
        self.assertEqual(calculate_expression("10-25"), "-15")

    def test_multiplication(self):
        self.assertEqual(calculate_expression("6*7"), "42")
        self.assertEqual(calculate_expression("-4*5"), "-20")

    def test_division(self):
        self.assertEqual(calculate_expression("81/9"), "9")
        self.assertEqual(calculate_expression("1/4"), "0.25")

    def test_zero_division(self):
        self.assertEqual(calculate_expression("42/0"), "Error: Div/0")
        self.assertEqual(calculate_expression("0/0"), "Error: Div/0")

    def test_syntax_error_handling(self):
        self.assertEqual(calculate_expression("12++"), "Error")
        self.assertEqual(calculate_expression("abc"), "Error")

if __name__ == "__main__":
    unittest.main()
