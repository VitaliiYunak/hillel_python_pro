from pymongo import MongoClient


def crud_mssql():
    """
    Операції CRUD для MSSQL
    """
    # Create
    sql_create = """
    INSERT INTO Products (id, name, price, category, stock)
    VALUES (NEWID(), "Lenovo IdeaPad Slim 5", "24999.00", "Ноутбуки", 3)
    """

    # Read
    sql_read = """
    SELECT * FROM Products WHERE id = '6F9619FF-8B86-D011-B42D-00C04FC964FF'
    """

    # Update
    sql_update = """
    UPDATE Products SET stock = 5 WHERE id = '6F9619FF-8B86-D011-B42D-00C04FC964FF'
    """

    # Delete
    sql_delete = """
    DELETE FROM Products WHERE id = '6F9619FF-8B86-D011-B42D-00C04FC964FF'
    """


def crud_mongodb():
    """
    Операції CRUD для MongoDB
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['online']
    product = db['products']

    # Create
    product.insert_one(
            {"_id": 1,
             "name": "Lenovo IdeaPad Slim 5",
             "price": 24999.00,
             "category": "Ноутбуки",
             "stock": 3}
            )

    # Read
    product.find_one({"_id": 1})

    # Update
    product.update_one(
        {"_id": 1},
        {"$set": {"stok": 5}}
    )

    # Delete
    product.delete_one({"_id": 1})


"""
Переваги та недоліки кожної системи для різних завдань.

MSSQL (Реляційна база даних)
Переваги:
Підтримує транзакції, що забезпечує цілісність даних.
Можливість виконання складних SQL-запитів з приєднаннями (joins).
Чітка схема полегшує роботу з структурованими даними.
Недоліки:
Гнучкість: Складно змінювати структуру таблиць.
Масштабування: Горизонтальне масштабування може бути складнішим.

MongoDB (NoSQL база даних)
Переваги:
Легко змінювати структуру документів, додаючи або видаляючи поля.
Легко масштабувати.
Висока швидкість читання/запису для великих обсягів даних.
Недоліки:
Обмежена підтримка транзакцій.
Складні запити менш зручні.
"""