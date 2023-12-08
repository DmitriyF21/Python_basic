"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data
#Внутри ф-и вызываем асинхронный менеджер, в нем открываем сессию через aiohttp, и следующим шагом
# посылаем запрос GET по url session.get(url).
# Результат кладем в переменную response и возвращаем его, преобразовав в json (return await response.json())
# — код с return читается справа налево. Вначале await переменной, затем return того, что получилось)
if __name__ == "__main__":
    asyncio.run(fetch_json(USERS_DATA_URL))





