from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel
from db import engine, get_session
from models import UserCreate, UserRead, User
import crud
from sqlmodel import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Crear tablas
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    return crud.create_user(session, user)

@app.get("/users/", response_model=list[UserRead])
def read_users(session: Session = Depends(get_session)):
    return crud.get_users(session)

@app.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = crud.get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user