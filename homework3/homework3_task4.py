# 4. Binary

class BinaryNumber:
    """
    Методи для виконання двійкових операцій: AND (__and__), OR (__or__), XOR (__xor__) та NOT (__invert__)
    """
    def __init__(self, x):
        self.x = x

    # Двійкова операція AND
    def __and__(self, other):
        if not isinstance(other, BinaryNumber):
            raise ValueError("Коректно вказуйте координати")
        return self.x & other.x

    # Двійкова операція OR
    def __or__(self, other):
        if not isinstance(other, BinaryNumber):
            return ValueError("Коректно вказуйте координати")
        return self.x | other.x

    # Двійкова операція XOR
    def __xor__(self, other):
        if not isinstance(other, BinaryNumber):
            return ValueError("Коректно вказуйте координати")
        return self.x ^ other.x

    # Двійкова операція INVERT
    def __invert__(self):
        return ~self.x

    def __str__(self):
        return f"Number:{self.x}"


try:
    bn1 = BinaryNumber(3)
    bn2 = BinaryNumber(5)
    print(f"{bn1}, {bn2}")
    print(f"Результат двійкової операції AND:", bn1 & bn2)
    print(f"Результат двійкової операції OR:", bn1 | bn2)
    print(f"Результат двійкової операції XOR:", bn1 ^ bn2)
    print(f"Результат двійкової операції INVERT:", ~bn1)
except ValueError as e:
    print(e)
