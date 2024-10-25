# Завдання 3: Асинхронні черги

import asyncio


async def producer(queue: asyncio.Queue):
    """
    Додає 5 завдань до черги із затримкою в 1 секунду.
    """
    for turn in range(5):
        task = turn + 1
        await queue.put(task)
        print(f"Завдання : {task}")
        await asyncio.sleep(1)


async def consumer(queue: asyncio.Queue, consumer_id: int):
    """
    Отримує завдання з черги. Працює до отримання None, що вказує на завершення.
    """
    while True:
        task = await queue.get()
        if task is None:
            break
        print(f"Споживач {consumer_id} обробляє завдання: {task}")
        await asyncio.sleep(2)
        queue.task_done()


async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))

    consumers = []
    for i in range(1, 4):
        consumers.append(asyncio.create_task(consumer(queue, i)))

    await producer_task

    for _ in consumers:
        await queue.put(None)

    await asyncio.gather(*consumers)


if __name__ == "__main__":
    asyncio.run(main())
