from fastapi import FastAPI, Request
from app import api

import time

app = FastAPI()

def create_app(app: FastAPI):
    app.include_router(api.router)

create_app(app)


@app.middleware('http')
async def session_identifier(request: Request, call_next):
    start = time.time()

    response = await call_next(request)
    process_time = time.time() - start

    response.headers['X-Process-Time'] = str(process_time)
    return response