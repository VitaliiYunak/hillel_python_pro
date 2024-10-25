# Завдання 1: Основи асинхронності

import asyncio
import random


async def download_page(url: str):
    """Завантаження сторінки за випадковий проміжок часу
    """
    load_time = random.randint(1, 5)
    await asyncio.sleep(4)
    print(f" Сторінка '{url}' завантажена за {load_time} секунд(и)")


async def main(urls: list):
    """
    Приймає список з декількох URL і завантажує їх одночасно, використовуючи await для
    паралельного виконання
    :param urls: список url
    """
    list_url = []
    for url in urls:
        list_url.append(download_page(url))
    # Виконання задач паралельно
    await asyncio.gather(*list_url)


if __name__ == "__main__":
    urls = [
        "https://vintest.org.ua/zno/zno-inform/",
        "https://testportal.gov.ua/osnovne-pro-byefvv/",
        "https://testportal.gov.ua/osnovne-pro-magisterski-vyprobuvannya-3/",
        "https://testportal.gov.ua/zagagalna-informatsiya-pedahog/"
    ]
    asyncio.run(main(urls))
