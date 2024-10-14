"""Завдання 4. Тестування з використанням doctest
"""


def is_even(n: int) -> bool:
    """
    Перевіряє, чи є число парним.

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-2)
    True
    >>> is_even(-3)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Повертає факторіал числа.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    """
    if n < 0:
        raise ValueError("Факторіал не може бути визначений для від’ємних чисел.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
