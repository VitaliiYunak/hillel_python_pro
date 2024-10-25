# Завдання 4: Асинхронний таймаут

import asyncio


async def slow_task():
    """
     Виконанує завдання протягом 10 секунд.
    """
    print("Початок виконання завдання")
    await asyncio.sleep(10)
    print("Завдання виконано")


async def main():
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Перевищено час очікування")


if __name__ == "__main__":
    asyncio.run(main())
