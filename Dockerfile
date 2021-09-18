FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /app/

COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH=/app
