from app.exception.business_exception import BusinessException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

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


@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(status_code=400, content={"message": f"Error {exc.name}!!"})