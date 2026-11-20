def calculator(a, b, operation):
    """
    Выполняет базовую арифметическую операцию.

    :param a: первое число
    :param b: второе число
    :param operation: строка с операцией ('add', 'subtract', 'multiply', 'divide')
    :return: результат операции
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    else:
        raise ValueError(f"Неизвестная операция: {operation}")