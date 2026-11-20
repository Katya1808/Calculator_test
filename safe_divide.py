def safe_divide(a, b):
    """
    Безопасное деление двух чисел.

    :param a: делимое
    :param b: делитель
    :return: результат деления a на b
    :raises ZeroDivisionError: если b равно нулю
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b