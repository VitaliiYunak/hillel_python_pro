# Завдання 7: Порівняння багатопотоковості/багатопроцесорності/асинхронності

import requests
import time
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor


# Синхронний режим
def synchronous():
    url = "https://vintest.org.ua/"
    for i in range(500):
        response = requests.get(url)
        print(f"{i}: {response.status_code}")


# Багатопоточний режим
def thread():
    url = "https://vintest.org.ua/"
    response = requests.get(url)
    return response.status_code


def threaded_requests():
    with ThreadPoolExecutor(max_workers=20) as execut:
        execut.map(thread, range(500))


# Асинхронний режим
async def asynchronous(session):
    url = "https://vintest.org.ua/"
    async with session.get(url) as response:
        return response.status


async def asynchronous_requests():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(500):
            tasks.append(asynchronous(session))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    synchronous()
    end_time = time.time()
    print(f"Синхронний режим: {end_time - start_time:.2f} секунд")

    start_time = time.time()
    threaded_requests()
    end_time = time.time()
    print(f"Багатопоточний режим: {end_time - start_time:.2f} секунд")

    start_time = time.time()
    asyncio.run(asynchronous_requests())
    end_time = time.time()
    print(f"Асинхронний режим: {end_time - start_time:.2f} секунд")
