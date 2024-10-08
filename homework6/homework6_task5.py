# Завдання 5: Робота з XML
import xml.etree.ElementTree as et


def read_products(file_path):
    """
    Виводить назви продуктів і їхню кількість.
    :param file_path: назва файлу
    """
    tree = et.parse(file_path)
    root = tree.getroot()

    products = []
    for product in root.findall('product'):
        name = product.find('name').text
        quantity = product.find('quantity').text
        products.append((name, quantity))
    return products


def update_quantity(file_path, product_name, new_quantity):
    """
    Змінює кількість для продукту, виводить оновлені дані.
    """
    tree = et.parse(file_path)
    root = tree.getroot()

    for product in root.findall('product'):
        name = product.find('name').text
        if name == product_name:
            product.find('quantity').text = str(new_quantity)
            break

    tree.write(file_path)


if __name__ == "__main__":

    # Зчитування інформації з XML-файлу
    filepath = 'products.xml'
    products = read_products(filepath)

    # Виведення назв продуктів та їхньої кількості
    for name, quantity in products:
        print(f"Продукт: {name}, кількість: {quantity}")

    # Зміна кількості товару
    product_to_update = "Хліб"
    new_quantity = 110
    update_quantity(filepath, product_to_update, new_quantity)

    # Виведення оновлених даних
    updated_products = read_products(filepath)
    print("Змінена кількість товару:")
    for name, quantity in updated_products:
        print(f"Продукт: {name}, кількість: {quantity}")
