# FastAPI Template

This template have several thing to make you start project with SQLAlchemy easier.

## Requirement

`Python >= 3.6`

## Installation
```
$ pip install -r requirements.txt
```

## Configuration
First time you need to config `.env` to connect to your database

```
 - db_username 
 - db_pwd
 - db_name
 - db_port
```

## First time started
```
$ uvicorn app.main:app --reload
```

After run command server will start [FastAPI](localhost:8000) with Port `8000`