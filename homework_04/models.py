import datetime
import os
from sqlalchemy.pool import NullPool
from sqlalchemy import (
Integer,
String,
Column,
DateTime,
ForeignKey)
# импортируем асинхронные методы sqlalchemy для работы с БД
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
# импортируем метод работы с бд, фабрику сессий и связи
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DB_URL = 'postgresql+asyncpg://user:password@localhost:5432/postgres'
PG_CONN_URI = (os.environ.get("SQLALCHEMY_PG_CONN_URI") or DB_URL)
engine = create_async_engine(PG_CONN_URI, echo=True, poolclass=NullPool)

# создаем метод описания БД (Создаем базовый класс для декларативных определений классов.)
Base = declarative_base()


async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column (String, nullable=False, default='')
    email = Column (String, nullable=False, default='')

    posts = relationship('Post',back_populates='user')

    def __str__(self):
        return f'{self.__classname__.name}(id{self.id},name{self.name!r},email{self.email!r})'

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default='')
    description = Column(String,nullable=False, default='')

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='post')

    def __str__(self):
        return f'{self.__class__.name}(id={self.id},title = {self.title}, body = {self.body}'

    def __repr__(self):
        return str(self)


async def save_user_in_db(u_data):
    async with async_session() as session:
        async with session.begin():
            for user in u_data:
                name = user['name']
                email = user ['email']
                user = User(name=name, email=email)
                session.add(user)


async def save_post_in_db(p_data):
    async with async_session() as session:
        async with session.begin():
            for post in p_data:
                title = post['title']
                description = post['body']
                user_id = post['userId']
                post = Post(title=title, description=description,user_id=user_id)
                session.add(post)


async def create_db_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)