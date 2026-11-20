import unittest
from calculator import calculator


class TestCalculator(unittest.TestCase):
    """Тесты для функции calculator."""

    # ===== Тесты на сложение =====
    def test_add_positive_numbers(self):
        """Сложение двух положительных чисел."""
        self.assertEqual(calculator(2, 3, 'add'), 5)

    def test_add_negative_numbers(self):
        """Сложение с отрицательным числом."""
        self.assertEqual(calculator(-1, -1, 'add'), -2)

    def test_add_zero(self):
        """Сложение с нулём."""
        self.assertEqual(calculator(5, 0, 'add'), 5)

    # ===== Тесты на вычитание =====
    def test_subtract_positive(self):
        """Вычитание положительных чисел."""
        self.assertEqual(calculator(10, 4, 'subtract'), 6)

    def test_subtract_negative_result(self):
        """Вычитание, дающее отрицательный результат."""
        self.assertEqual(calculator(3, 7, 'subtract'), -4)

    # ===== Тесты на умножение =====
    def test_multiply_positive(self):
        """Умножение положительных чисел."""
        self.assertEqual(calculator(3, 4, 'multiply'), 12)

    def test_multiply_by_zero(self):
        """Умножение на ноль."""
        self.assertEqual(calculator(5, 0, 'multiply'), 0)

    def test_multiply_negative(self):
        """Умножение отрицательных чисел."""
        self.assertEqual(calculator(-2, 3, 'multiply'), -6)

    # ===== Тесты на деление =====
    def test_divide_positive(self):
        """Деление положительных чисел."""
        self.assertEqual(calculator(10, 2, 'divide'), 5.0)

    def test_divide_fractional(self):
        """Деление с дробным результатом."""
        self.assertEqual(calculator(7, 2, 'divide'), 3.5)

    def test_divide_by_zero(self):
        """Деление на ноль должно вызывать ValueError."""
        with self.assertRaises(ValueError):
            calculator(10, 0, 'divide')

    # ===== Тест на невалидную операцию =====
    def test_invalid_operation(self):
        """Неизвестная операция должна вызывать ValueError."""
        with self.assertRaises(ValueError):
            calculator(1, 2, 'modulo')


if __name__ == '__main__':
    unittest.main()