from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')

# Створення бази даних
db = client['online']

# Створення колекцій
products = db['products']
orders = db['orders']

# Додавання продуктів
products.insert_many(
    [
        {"_id": 1,
         "name": "Lenovo IdeaPad Slim 5",
         "price": 24999.00,
         "category": "Ноутбуки",
         "stock": 3},
        {"_id": 2,
         "name": "Acer Aspire 7",
         "price": 33999.00,
         "category": "Ноутбуки",
         "stock": 1},
        {"_id": 3,
         "name": "Samsung Odyssey DG50",
         "price": 10299.00,
         "category": "Монітори",
         "stock": 4}
    ]
)

# Додавання замовлень
orders.insert_many(
    [
        {"_id": 1,
         "number": 1,
         "data_order": datetime.now(),
         "customer": "Микита Мельник",
         "products": [{"name": "Acer Aspire 7", "quantity": 1}],
         "total": 33999.00},
        {"_id": 2,
         "number": 2,
         "data_order": datetime.now(),
         "customer": "Ольга Люлько",
         "products": [{"name": "Samsung Odyssey DG50", "quantity": 2}],
         "total": 20598.00}
    ]
)

# Оновлення кількості продукту
products.update_one(
    {"name": "Acer Aspire 7"},
    {"$inc": {"stock": -1}}
)

# Оновлення кількості продукту
products.update_one(
    {"name": "Samsung Odyssey DG50"},
    {"$inc": {"stock": -2}}
)

# Замовлення за останні 30 днів
all_orders = orders.find({"data_order": {"$gte": datetime.now() - timedelta(days=30)}})
if all_orders:
    for order in all_orders:
        print(order)
else:
    print("Нічого не знайдено")

# Видалення продуктів, які більше не доступні для продажу.
products.delete_many({"stock": 0})

# Кількість проданих продуктів за певний період часу.
numbers_of_products_sold = orders.aggregate(
    [
        {"$unwind": "$products"},
        {"$group": {"_id": "$products.name",
                    "Кількість проданого товару": {"$sum": "$products.quantity"}}}
    ])
for product in numbers_of_products_sold:
    print(product)

# Загальна сума замовлень клієнта
total_summa = orders.aggregate([
    {"$match": {"customer": "Ольга Люлько"}},
    {"$group": {"_id": "$customer", "Загальна сума замовлень": {"$sum": "$total"}}}
])
for summa in total_summa:
    print(summa)

# Додавання індексу для поля category в колекції products
products.create_index([("category", 1)])
