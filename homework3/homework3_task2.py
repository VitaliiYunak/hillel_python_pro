# 2.  Numeric-like

import math


class Vector:
    """
    Підтримуються операції з векторами: додавання, віднімання, множення на число та порівняння за довжиною.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Додає вектори
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Коректно вказуйте координати")
        return Vector(self.x + other.x, self.y + other.y)

    # Віднімає один вектор від іншого
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Коректно вказуйте координати")
        return Vector(self.x - other.x, self.y - other.y)

    # Множить вектор на число
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise ValueError("Коректно вказуйте координати")

    # Обчислює довжину вектора
    def len_of_vector(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Порівнює довжини векторів
    def __lt__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Коректно вказуйте координати")
        return self.len_of_vector() < other.len_of_vector()

    # Порівнює два вектори, чи дорівнюють їх координати
    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Коректно вказуйте координати")
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Вектор({self.x}, {self.y})"


vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

print(repr(vector1))
print(repr(vector2))
print(f"Додавання {vector1} + {vector2}:", vector1 + vector2)
print(f"Віднімання {vector2} - {vector1}:", vector2 - vector1)
print(f"Множення {vector1} на 3:", vector1 * 3)
print(f"Множення {vector2} на 4:", vector2 * 4)
print(f"Довжина {vector1}: {vector1.len_of_vector()}")
print(f"Довжина {vector2}: {vector2.len_of_vector()}")
print(f"Чи вектор {vector1} < {vector2}:", vector1 < vector2)
print(f"Чи вектор {vector2} < {vector1}:", vector2 < vector1)
print(f"Чи дорівнюють вектор один одному:", vector1 == vector2)
