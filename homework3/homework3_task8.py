# 8. Price class discussion before the PaymentGateway implementation

class Price:
    """
    Визначає ціну товару з можливістю заокруглення до двох десяткових знаків.
    Обчислює загальну ціну товарів, порівнює ціни.
    """
    def __init__(self, suma: float):
        if isinstance(suma, float):
            self.suma = round(suma, 2)

    def __add__(self, other):
        if isinstance(other, Price):
            return Price(self.suma + other.suma)
        return ValueError

    def __sub__(self, other):
        if isinstance(other, Price):
            return Price(self.suma - other.suma)
        return ValueError

    def __eq__(self, other):
        if isinstance(other, Price):
            return self.suma == other.suma
        return ValueError

    def __lt__(self, other):
        if isinstance(other, Price):
            return self.suma < other.suma
        return ValueError

    def __str__(self):
        return f"{self.suma:.2f} грн."


try:
    sum1 = Price(1200.00)
    sum2 = Price(3000.00)
    print("Загальна ціна товарів:", sum1 + sum2)
    print("Другий товар дешевше першого?:", sum2 < sum1)
except ValueError as e:
    print(e)

"""
Клас Price може бути використаний в майбутньому класі PaymentGateway для обробки фінансових транзакцій, а саме
- обчислювати загальну суму товарів;
- порівнювати ціни товарів;
- вираховувати, чи достатньо коштів для здійснення покупки.
"""
