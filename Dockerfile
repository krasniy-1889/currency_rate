FROM python:3.12.1

WORKDIR /code

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .