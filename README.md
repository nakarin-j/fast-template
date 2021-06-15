# __FastAPI Template__

This template have several thing to make you start project with SQLAlchemy easier.

## __Requirement__

`Python >= 3.6`

## __Installation__
```
$ pip install -r requirements.txt
```

## __Configuration__
First time you need to config `.env` to connect to your database

```
 - db_username 
 - db_pwd
 - db_name
 - db_port
```

## __First time started__

First time after config database detail. You need to create database and create table with `Alembic` command
```
alembic upgrade head
```

## __Get started__

```
$ uvicorn app.main:app --reload
```

After run command server will start [FastAPI](localhost:8000) with Port `8000`

___

## __Create migration Script__
If you want to add new table you can use `Alembic` to autogenerate migration script

```
alembic revision --autogenerate -m <message>
```

and upgrade database with __command__

```
alembic upgrade head
```
## __Downgrade Version__

If you want to downgrade version of `Alembic` you can use with __command__
```
alembic downgrade -1
```
