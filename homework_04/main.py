"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from jsonplaceholder_requests import USERS_DATA_URL, POSTS_DATA_URL, fetch_json
from models import engine, Base, Session, User, Post, connect_db


async def create_db_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.drop_all)


async def save_user_in_db(u_data):
    async with Session as session:
        async with session.begin():
            for user in u_data:
                name = user['name']
                email = user ['email']
                user = User(name=name, email=email)
                session.add(user)


async def save_post_in_db(p_data):
    async with Session as session:
        async with session.begin():
            for post in p_data:
                title = post['title']
                description = post['description']
                post = Post(title=title, description=description)
                session.add(post)


async def async_main():
    await connect_db()
    await create_db_tables()
    user_data, post_data = await asyncio.gather(fetch_json(USERS_DATA_URL), fetch_json(POSTS_DATA_URL))
    await save_user_in_db(user_data)
    await save_post_in_db(post_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
