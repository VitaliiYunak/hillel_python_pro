# 7. Vector class implementation
import math


class Vector:
    """
    Представляє вектор у просторі з n вимірами. Додає, порівнює вектори, обчислення скалярний добуток.
    """
    def __init__(self, *args):
        self.components = args
        self.dimension = len(args)

    # Додає вектори
    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Має бути однаковий розмір.")
        result = []
        for i, j in zip(self.components, other.components):
            result.append(i + j)
        return Vector(*result)

    # Віднімає один вектор від іншого
    def __sub__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Має бути однаковий розмір.")
        result = []
        for i, j in zip(self.components, other.components):
            result.append(i - j)
        return Vector(*result)

    # Обчислює довжину вектора
    def length(self):
        result = 0
        for i in self.components:
            result += math.sqrt(i ** 2)
        return result

    # Порівнює довжини векторів
    def __lt__(self, other):
        return self.length() < other.length()

    # Скалярний добуток векторів
    def __mul__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Має бути однаковий розмір.")
        result = 0
        for i, j in zip(self.components, other.components):
            result += i * j
        return result

    def __str__(self):
        return f"V({', '.join(map(str, self.components))})"


try:
    v1 = Vector(7, 8, 9)
    v2 = Vector(4, 5, 6)
    print(v1)
    print(v2)
    print("Результат додавання векторів:", v1 + v2)
    print("Результат віднімання векторів:", v1 - v2)
    print("Скалярний добуток:", v1 * v2)
    print("Перший вектор менший за другий?:", v1 < v2)
except ValueError as e:
    print(e)
