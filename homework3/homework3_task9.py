class ProductWithGetSet:
    """
    Встановлює назву товару та ціну через сеттер/геттер. Дає можливість змінити ціну товара.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        self.__price = price


class ProductWithProperty:
    """
    Встановлює назву товару та ціну через декоратор @property. Дає можливість змінити ціну товара.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        self.__price = price


class Descriptor:
    def __get__(self, instance, owner):
        return instance.__price

    def __set__(self, instance, price: float):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        instance.__price = price


class ProductWithDescriptor:
    """
    Встановлює назву товару та ціну через декоратори. Дає можливість змінити ціну товара.
    """
    price = Descriptor()

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


try:
    product1 = ProductWithGetSet("Ноутбук", 32400.00)
    print(f"{product1.name}. Ціна: {product1.get_price()}")
    product1.set_price(30400.00)
    print(f"{product1.name}. Нова ціна: {product1.get_price()}")

    product2 = ProductWithProperty("Принтер", 8300.00)
    print(f"{product2.name}. Ціна: {product2.price}")
    product2.price = 8100.00
    print(f"{product2.name}. Нова ціна: {product2.price}")

    product3 = ProductWithDescriptor("Монітор", 4000.00)
    print(f"{product3.name}. Ціна: {product3.price}")
    product3.price = 4100.00
    print(f"{product3.name}. Нова ціна: {product3.price}")

    product1.set_price(-1200.00)
    product2.price = -8100.00
    product3.price = -4100.00
except ValueError as e:
    print(e)

"""
Декоратор @property:
Як на мене, найзручніший спосіб. Має лаконічний вигляд, легкий для розуміння.
Сеттери/геттери: 
Простий спосіб у реалізації, але може бути більш об'ємним у виконанні.
Дескриптори:
Більш  об'ємним у виконанні, складніший у реалізації, важче зрозуміти. 
"""
