# Завдання 1: Створення власного пакету

def factorial(n):
    """
    Обчислює факторіал числа
    """
    if n < 0:
        raise ValueError("Факторіал не визначений для від'ємних чисел.")
    if n == 0 or n == 1:
        return f"Факторіал числа {n} дорівнює: 1"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return f"Факторіал числа {n} дорівнює: {result}"


def greatest_denominator(a, b):
    """
    Знаходить найбільший спільний дільник двох чисел.
    """
    str_for_result = f"Найбільший спільний дільник чмсел {a} та {b}"
    while a * b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return f"{str_for_result}: {a + b}"


if __name__ == "__main__":
    print(factorial(3))
    print(greatest_denominator(9, 27))
