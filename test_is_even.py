import unittest
from is_even import is_even


class TestIsEven(unittest.TestCase):
    """Параметрические тесты для функции is_even."""

    def test_is_even_with_various_numbers(self):
        """
        Параметрический тест: проверяем чётность на наборе чисел.
        Используем subTest, чтобы каждый случай был независимым.
        """
        # Набор тестовых данных: (число, ожидаемый результат)
        test_cases = [
            # Положительные чётные
            (2, True),
            (4, True),
            (100, True),
            (1000, True),
            # Положительные нечётные
            (1, False),
            (3, False),
            (99, False),
            # Отрицательные чётные
            (-2, True),
            (-4, True),
            (-100, True),
            # Отрицательные нечётные
            (-1, False),
            (-3, False),
            (-99, False),
            # Ноль (чётное число!)
            (0, True),
        ]

        for num, expected in test_cases:
            with self.subTest(num=num, expected=expected):
                self.assertEqual(
                    is_even(num),
                    expected,
                    msg=f"Число {num} должно быть {'чётным' if expected else 'нечётным'}"
                )


if __name__ == '__main__':
    unittest.main()