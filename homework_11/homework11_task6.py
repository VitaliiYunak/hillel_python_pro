# Завдання 6: Завантаження зображень з декількох сайтів

import aiohttp
import asyncio


async def download_image(url: str, filename: str):
    """
    :param url: URl зображення
    :param filename: назва файлу для збереження
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, 'wb') as f:
                    f.write(await response.read())
                print(f"Файл '{filename}' завантажено")
            else:
                print(f"Не вдалося завантажити {url}. Cтатус {response.status}")


async def main():
    image_urls = [
        ("https://elle.ua/upload/image/photo1661171584.jpeg", "photo1661171584.jpeg"),
        ("https://elle.ua/upload/image/photo1661172154.jpeg", "photo1661172154.jpeg"),
        ("https://elle.ua/upload/image/photo1661198444.jpeg", "photo1661198444.jpeg"),
        ("https://elle.ua/upload/image/photo1661169309.jpeg", "photo1661169309.jpeg"),
        ("https://elle.ua/upload/image/photo1661175949.jpeg", "photo1661175949.jpeg"),
        ("https://elle.ua/upload/image/photo1.jpeg", "photo1.jpeg"),
    ]

    tasks = []
    for url, filename in image_urls:
        tasks.append(download_image(url, filename))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
