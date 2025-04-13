from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routes import router
from .database import create_db_and_tables



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("Sayonaraaaa!")

app = FastAPI(lifespan=lifespan)

# app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(router, prefix="/items", tags=["Items"])