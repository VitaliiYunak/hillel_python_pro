"""
Консольний застосунок для керування базою даних "Кінобаза", що містить інформацію
про фільми та акторів, які в них знімалися.
"""
import re
import sqlite3
import datetime


def connect_db():
    """
    Підключення до бази даних
    """
    return sqlite3.connect('cinema.db')


def create_tables():
    """
    Створення бази даних і таблиць
    """

    try:
        connection = connect_db()
        cursor = connection.cursor()
        create_table_movies = """
                            CREATE TABLE IF NOT EXISTS movies (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            release_year INTEGER NOT NULL,
                            genre TEXT NOT NULL)"""
        cursor.execute(create_table_movies)

        create_table_actors = """
                            CREATE TABLE IF NOT EXISTS actors (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            birth_year INTEGER NOT NULL)"""
        cursor.execute(create_table_actors)

        create_table_movie_cast = """
                                CREATE TABLE IF NOT EXISTS movie_cast (
                                movie_id INTEGER,
                                actor_id INTEGER,
                                PRIMARY KEY (movie_id, actor_id),
                                FOREIGN KEY (movie_id) REFERENCES movies (id),
                                FOREIGN KEY (actor_id) REFERENCES actors (id))"""
        cursor.execute(create_table_movie_cast)
        connection.commit()
        cursor.close()
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def add_movie():
    """
    Додавання нового фільму з акторами.
    """
    print("-" * 20)
    title = input("Введіть назву фільму: ")

    while True:
        try:
            release_year = input("Введіть рік випуску: ")
            pattern = r'\b(19|20)\d{2}\b'
            if re.findall(pattern, release_year):
                break
            else:
                print("Перші дві цифри року випуску повинні бути 19 або 20")
        except ValueError as e:
            print(e)

    genre = input("Введіть жанр: ")

    try:
        connection = connect_db()
        cursor = connection.cursor()

        sql_movie = """INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)"""
        data_movie = (title, release_year, genre)
        cursor.execute(sql_movie, data_movie)
        movie_id = cursor.lastrowid

        sql_actors = """SELECT id, name FROM actors"""
        cursor.execute(sql_actors)
        all_actors = cursor.fetchall()
        id_actors = []
        for actor in all_actors:
            id_actors.append(actor[0])
            print(f"№{actor[0]} - {actor[1]}")

        while True:
            actor_id = int(input("Введіть № актора (0 для завершення): "))
            if actor_id == 0:
                break
            if actor_id in id_actors:
                sql_actors_for_movie = """INSERT INTO movie_cast (movie_id, actor_id) 
                                        VALUES (?, ?)"""
                data_actors_for_movie = (movie_id, actor_id)
                cursor.execute(sql_actors_for_movie, data_actors_for_movie)
            else:
                print(f"Актор з №{actor_id} відсутній")
        connection.commit()
        cursor.close()
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def add_actor():
    """
    # Додавання актора
    """
    print("-" * 20)
    name = input("Введіть ім'я актора: ")
    while True:
        try:
            birthday_year = input("Введіть рік народження актора: ")
            pattern = r'\b(18|19|20)\d{2}\b'
            if re.findall(pattern, birthday_year):
                break
            else:
                print("Перші дві цифри року народження повинні бути 18, 19 або 20")
        except ValueError as e:
            print(e)
    try:
        connection = connect_db()
        cursor = connection.cursor()
        sql = """INSERT INTO actors (name, birth_year) VALUES (?, ?)"""
        cursor.execute(sql, (name, birthday_year))
        connection.commit()
        cursor.close()
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def show_movies_with_actors():
    """Усі фільми з акторами
    """
    print("-" * 20)
    try:
        connection = connect_db()
        cursor = connection.cursor()
        sql = """
                SELECT M.title, GROUP_CONCAT(A.name, ', ')
                FROM movies M
                INNER JOIN movie_cast MC ON M.id = MC.movie_id
                INNER JOIN actors A ON MC.actor_id = A.id
                GROUP BY M.id"""
        cursor.execute(sql)
        movies = cursor.fetchall()
        cursor.close()
        if movies:
            print("Фільми та актори:")
            for movie, actors in movies:
                print(f'Фільм: "{movie}", Актори: {actors}')
        else:
            print("Відсутні фільми")
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def show_unique_genres():
    """ Унікальні жанри
    """
    print("-" * 20)
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""SELECT DISTINCT genre FROM movies""")
        genres = cursor.fetchall()
        cursor.close()
        print("Жанри:")
        for genre in genres:
            print(genre[0])
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def count_movies_by_genre():
    """Кількість фільмів за жанром
    """
    print("-" * 20)
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""SELECT genre, COUNT(id) AS count FROM movies GROUP BY genre""")
        counts = cursor.fetchall()
        print("Жанри та кількість фільмів:")
        for genre, count in counts:
            print(f"{genre}: {count}")
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def avg_birth_year_actors_by_genre():
    """ Середній рік народження акторів у фільмах певного жанру
    """
    print("-" * 20)
    try:
        genre = input("Введіть жанр: ")
        connection = connect_db()
        cursor = connection.cursor()
        sql = """
            SELECT AVG(A.birth_year)
            FROM actors A
            INNER JOIN movie_cast MC ON A.id = MC.actor_id
            INNER JOIN movies M ON MC.movie_id = M.id
            WHERE M.genre = ?
            """
        cursor.execute(sql, (genre,))
        avg_year = cursor.fetchone()[0]
        cursor.close()
        print(f'Середній рік народження акторів у жанрі "{genre}": {int(avg_year)}')
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def search_movie_by_title():
    """Пошук фільму за назвою
    """
    print("-" * 20)
    word_for_search_movie = input("Введіть ключове слово для пошуку: ")
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""SELECT title FROM movies WHERE title LIKE ?""",
                       ('%' + word_for_search_movie + '%',))
        movies = cursor.fetchall()
        cursor.close()
        print("Знайдені фільми:")
        for movie in movies:
            print(movie[0])
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def show_movies_with_pagination():
    """Фільми з пагінацією
    """
    print("-" * 20)
    page = int(input("Введіть номер сторінки: "))
    limit = 3
    offset = (page - 1) * limit
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""SELECT title FROM movies LIMIT ? OFFSET ?""", (limit, offset))
        movies = cursor.fetchall()
        cursor.close()
        for movie in movies:
            print(movie[0])
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def show_actors_and_movies():
    """Імена всіх акторів та назви всіх фільмів
    """
    print("-" * 20)
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT title FROM movies
                        UNION
                        SELECT name FROM actors
                        """)
        results = cursor.fetchall()
        cursor.close()
        for result in results:
            print(result[0])
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def movie_age(year):
    """Обчислення віку фільму
    """
    return datetime.datetime.now().year - year


def show_movies_with_age():
    """Фільми та їх вік
    """
    print("-" * 20)
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""SELECT title, release_year FROM movies""")
        movies = cursor.fetchall()
        for title, year in movies:
            age = movie_age(year)
            print(f'Фільм: "{title}" — {age} роки(ів)')
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()


def main_menu():
    """ Основне меню
    """
    create_tables()
    while True:
        print("-" * 20)
        print("Меню:")
        print("1. Додати фільм")
        print("2. Додати актора")
        print("3. Показати всі фільми з акторами")
        print("4. Показати унікальні жанри")
        print("5. Показати кількість фільмів за жанром")
        print("6. Показати середній рік народження акторів у фільмах певного жанру")
        print("7. Пошук фільму за назвою")
        print("8. Показати фільми (з пагінацією)")
        print("9. Показати імена всіх акторів та назви всіх фільмів")
        print("0. Вихід")
#
        try:
            choice = int(input("Виберіть дію: "))
            if choice == 1:
                add_movie()
            elif choice == 2:
                add_actor()
            elif choice == 3:
                show_movies_with_actors()
                show_movies_with_age()
            elif choice == 4:
                show_unique_genres()
            elif choice == 5:
                count_movies_by_genre()
            elif choice == 6:
                avg_birth_year_actors_by_genre()
            elif choice == 7:
                search_movie_by_title()
            elif choice == 8:
                show_movies_with_pagination()
            elif choice == 9:
                show_actors_and_movies()
            elif choice == 0:
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")
        except ValueError:
            print("Щось пішло не так. Спробуйте ще раз")


if __name__ == "__main__":
    main_menu()
