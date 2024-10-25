# Завдання 2: Робота з асинхронними HTTP-запитами

import aiohttp
import asyncio


async def fetch_content(url: str):
    """
    Виконує HTTP-запит до url і повертає вміст сторінки.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientError as e:
        return f"Помилка підключення до {url}: {e}"


async def fetch_all(urls: list):
    """
    Приймає список urls і завантажує вміст усіх сторінок паралельно.
    """
    tasks = []
    for url in urls:
        tasks.append(fetch_content(url))
    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    urls = [
        "https://vintest.org.ua/pro-vrc/",
        "https://vintest.org.ua/kontakti/",
        "https://vintest.org.ua/korisni-linki/",
        # Помилка
        "https://vintest.org.ua/vintest/"
    ]
    result = asyncio.run(fetch_all(urls))

    for url, content in zip(urls, result):
        print(f"URL {url}:\n{content}\n")
