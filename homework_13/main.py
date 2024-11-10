import requests
from bs4 import BeautifulSoup
import pandas


def get_page(url):
    """ завантаження HTML-коду сторінки
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Викликає помилку, якщо код відповіді не 200
        return BeautifulSoup(response.text, 'lxml')
    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return None


def parse_news(soup):
    """
    :param soup: обЄєкт сторінки
    :return: словник news_list із ключами title, link, time, summary
    """
    news_list = []
    try:
        search_tags = soup.find_all("section", class_="im")
        if search_tags:
            for element in search_tags:
                date = element.time.text if element.time else "Немає часу"
                title = ' '.join(element.a.text.split()) if element.a.text else "Немає заголовка"
                link = element.a["href"] if element.a else "Немає посилання"
                summary = element.p.text if element.p else "Немає опису"
                news_list.append(
                    {
                        "time": date,
                        "title": title,
                        "link": link,
                        "summary": summary,
                    }
                )
    except Exception as e:
        print(f"Помилка при парсингу новин: {e}")
    return news_list


def save_to_csv(news_list, filename="news.csv"):
    """
    Приймає словник новин та зберігає його в CSV-файлі
    """
    try:
        pd = pandas.DataFrame(news_list)
        pd.to_csv(filename, index=False, encoding='utf-8', sep=";")
        print(f"Дані збережено в файл {filename}")
    except Exception as e:
        print(f"Помилка при збереженні в CSV: {e}")


def count_news(news_list):
    """
    Кількість новин за день на поточний час
    """
    try:
        pd = pandas.Series(news_list)
        return len(pd)
    except Exception as e:
        print(f"Трапилась помилка: {e}")


def main():
    url = "https://www.ukr.net/news/politics.html"
    soup = get_page(url)
    news_data = parse_news(soup)
    if news_data:
        save_to_csv(news_data)
        count = count_news(news_data)
        print(f"Кількість новин за день на поточний час: {count}")
    else:
        print("Новин не знайдено")


if __name__ == "__main__":
    main()
