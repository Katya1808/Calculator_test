import unittest
from safe_divide import safe_divide


class TestSafeDivide(unittest.TestCase):
    """Тесты функции safe_divide, включая проверку обработки ошибок."""

    # ===== Тесты на нормальную работу =====
    def test_divide_positive_numbers(self):
        """Деление двух положительных чисел."""
        self.assertEqual(safe_divide(10, 2), 5.0)

    def test_divide_negative_numbers(self):
        """Деление отрицательных чисел."""
        self.assertEqual(safe_divide(-10, -2), 5.0)

    def test_divide_fractional_result(self):
        """Деление с дробным результатом."""
        self.assertEqual(safe_divide(7, 2), 3.5)

    def test_divide_zero_numerator(self):
        """Деление нуля на число (результат = 0)."""
        self.assertEqual(safe_divide(0, 5), 0.0)

    # ===== Тесты на обработку ошибок =====
    def test_divide_by_zero_raises_exception(self):
        """
        Деление на ноль должно вызывать ZeroDivisionError.
        Используем assertRaises как контекстный менеджер.
        """
        with self.assertRaises(ZeroDivisionError):
            safe_divide(10, 0)

    def test_divide_by_zero_with_message(self):
        """
        Проверяем не только факт исключения, но и его сообщение.
        """
        with self.assertRaises(ZeroDivisionError) as context:
            safe_divide(10, 0)

        # Проверяем, что сообщение содержит ожидаемый текст
        self.assertIn("Деление на ноль", str(context.exception))

    def test_divide_by_zero_alternative_syntax(self):
        """
        Альтернативный синтаксис assertRaises (без with).
        Передаём функцию и аргументы напрямую.
        """
        self.assertRaises(ZeroDivisionError, safe_divide, 10, 0)

    # ===== Параметрический тест на деление на ноль =====
    def test_divide_by_zero_various_numerators(self):
        """
        Деление на ноль должно вызывать ошибку для любого делимого.
        Используем subTest для проверки нескольких случаев.
        """
        test_cases = [10, -5, 0, 100, 0.5]

        for num in test_cases:
            with self.subTest(num=num):
                with self.assertRaises(ZeroDivisionError):
                    safe_divide(num, 0)


if __name__ == '__main__':
    unittest.main()