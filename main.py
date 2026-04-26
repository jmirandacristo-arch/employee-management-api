from fastapi import FastAPI
from app.infrastructure.database.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from app.presentation.api.employee_router import router

#Create tables
Base.metadata.create_all(bind=engine)


#Create app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)