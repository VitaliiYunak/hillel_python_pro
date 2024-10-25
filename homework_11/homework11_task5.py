# Завдання 5: Створення простого асинхронного веб-сервера

from aiohttp import web
import asyncio


async def hello(request):
    """
    Повертає текст "Hello, World!".
    """
    return web.Response(text="Hello, World!")


async def slow(request):
    """
    Повертає текст "Operation completed" через 5 секунд затримки.
    """
    await asyncio.sleep(5)
    return web.Response(text="Operation completed")

app = web.Application()
app.router.add_get('/', hello)
app.router.add_get('/slow', slow)


if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
