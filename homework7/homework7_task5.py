""" Завдання 5. Тестування винятків у pytest (опціонально)
"""
import pytest


def divide(a: int, b: int) -> float:
    """
    Ділить два числа.
    """
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль не допускається.")
    return a / b


def test_divide_correct():
    """ Перевіряє коректне ділення.
    """
    assert divide(100, 50) == 2.0
    assert divide(-6, 3) == -2.0
    assert divide(-8, -4) == 2.0


def test_divide_zero():
    """ Перевіряє, чи виникає ZeroDivisionError, якщо знаменник дорівнює нулю.
    """
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize("a, b, result", [(100, 50, 2.0), (-6, 3, -2.0), (-8, -4, 2.0),])
def test_divide_parametrize(a, b, result):
    """
    Tест із параметризацією для перевірки поділу з різними значеннями.
    """
    assert divide(a, b) == result
