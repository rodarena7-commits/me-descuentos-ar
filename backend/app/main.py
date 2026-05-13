from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.database import engine, SessionLocal
from app.models import discount as discount_model
from app.routers import discounts
from app.scrapers.seed_data import SAMPLE_DISCOUNTS


def seed_db():
    db = SessionLocal()
    if db.query(discount_model.Discount).count() == 0:
        for data in SAMPLE_DISCOUNTS:
            db.add(discount_model.Discount(**data))
        db.commit()
    db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    discount_model.Base.metadata.create_all(bind=engine)
    seed_db()
    yield


app = FastAPI(
    title="Me — Descuentos Argentina",
    description="API para consultar descuentos, promociones y reintegros de bancos y fintechs argentinas.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "https://ahorrointeligente-ai.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(discounts.router)


@app.get("/")
def root():
    return {"message": "Me — Descuentos Argentina API", "docs": "/docs"}
