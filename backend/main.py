from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database.database import Base, engine
from backend.routers.router import router

app = FastAPI(title="MindMosaic AI Therapist API")

Base.metadata.create_all(bind=engine)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)