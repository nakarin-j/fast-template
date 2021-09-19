FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /app/

RUN mkdir log

COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

ENV PYTHONPATH=/app
