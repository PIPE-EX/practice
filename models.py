from typing import Optional
from sqlmodel import SQLModel, Field

# Modelo para la base de datos
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

# Modelo de entrada (para crear usuarios) con Pydantic
class UserCreate(SQLModel):
    name: str
    email: str

# Modelo de salida (respuesta en la API)
class UserRead(SQLModel):
    id: int
    name: str
    email: str