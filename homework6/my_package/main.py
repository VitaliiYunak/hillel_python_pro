# Завдання 1: Створення власного пакету

from math_utils import factorial, greatest_common_denominator
from string_utils import to_upper, strip_spaces


if __name__ == "__main__":
    print(to_upper("Hello, world!"))
    print(strip_spaces(" Hello, world!  "))
    print(factorial(3))
    print(greatest_common_denominator(9, 27))
