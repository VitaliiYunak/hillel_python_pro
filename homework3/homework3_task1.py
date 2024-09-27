from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменник не можу бути '0'")
        self.numerator = numerator
        self.denominator = denominator
        self.common_val()

    #  Зменшеня до найменших можливих значень
    def common_val(self):
        common_div = gcd(self.numerator, self.denominator)
        self.numerator //= common_div
        self.denominator //= common_div

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    # Додавання дробових чисел
    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    # Віднімання дробових чисел
    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Не можна ділити на 0.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"


fraction1 = Fraction(4, 5)
fraction2 = Fraction(7, 6)
print(fraction1)
print(fraction2)
try:
    print("Додавання:", fraction1 + fraction2)
    print("Віднімання:", fraction1 - fraction2)
    print("Множення:", fraction1 * fraction2)
    print("Ділення:", fraction1 / fraction2)
except ValueError as e:
    print(e)
