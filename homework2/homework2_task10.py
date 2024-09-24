# Завдання 10: Створення товарів для онлайн-магазину

def create_product(name, price, number):
    product = {
        "name": name,
        "price": price,
        "number": number
    }

    def set_new_price(price_new):
        nonlocal product
        product["price"] = price_new
        print(f"Нова ціна товару: {price_new}")

    def product_info():
        return product

    return set_new_price, product_info


new_price, get_product = create_product("Стіл", 2500, 10)

print("Інформація про товар:", get_product())

new_price(2800)

print("Оновлена інформація про товар:", get_product())
