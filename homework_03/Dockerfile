# Как запустить контейнер:docker run -p 8000:8000 my-web-server
# (как я понимаю таким образом докер внутри себя запускает веб сервер)
# После этого нужно  вместо любого запущенного хоста,будь то 8080 или 800 прописать localhost(127.0.0.1) и приложение заработает

FROM python:3.11 as requirements-stage

ENV PYTHONUNBUFFERED = 1

WORKDIR /tmp

RUN pip install --upgrade pip "poetry==1.6.1"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]





