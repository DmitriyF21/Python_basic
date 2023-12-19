"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import datetime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
Integer,
String,
Column,
DateTime,
ForeignKey)


SQLALCHEMY_PG_CONN_URI = 'postgresql+asyncpg://user:example@localhost:5432/blog'

engine = create_async_engine(SQLALCHEMY_PG_CONN_URI, echo=False)

# создаем метод описания БД (Создаем базовый класс для декларативных определений классов.)
Base = declarative_base()


Session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def connect_db():
    conn = await engine.connect()
    return conn


async def get_db() -> AsyncSession:
    async with Session() as session:
        yield session


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column (String, nullable=False, default='')
    email = Column (String, nullable=False, default='')
    stime = Column (DateTime,nullable=False, default=datetime.UTC)

    posts = relationship('Post',back_populates='user')

    def __str__(self):
        return f'{self.__classname__.name}(id{self.id},name{self.name!r},email{self.email!r},stime{self.stime!r})'

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default='')
    body = Column(String,nullable=False, default='')

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    users = relationship('User', back_populates='post')

    def __str__(self):
        return f'{self.__class__.name}(id={self.id},title = {self.title}, body = {self.body}'

    def __repr__(self):
        return str(self)


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