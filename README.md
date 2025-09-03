# FastAPI + PostgreSQL + React

Este proyecto es un ejemplo de aplicación **Fullstack** que incluye:

- **Backend:** FastAPI con Pydantic, SQLModel y SQLAlchemy  
- **Base de datos:** PostgreSQL  
- **Frontend:** React (interfaz simple para registrar y listar usuarios)  

---

## 🚀 Requisitos

- Python 3.10 o superior  
- PostgreSQL instalado y corriendo  
- Node.js y npm (para el frontend)  

---

## 📂 Estructura del proyecto
practica/
├── main.py # Punto de entrada FastAPI
├── db.py # Configuración de la base de datos
├── crud.py # Operaciones CRUD
├── models.py # Modelos SQLModel/Pydantic
├── init.py
│
├── frontend/ # React
│ ├── package.json
│ ├── src/
│ └── public/
│
└── teamplate/ # Plantilla HTML
└── index.html


---

## ⚙️ Configuración del backend

1. Crear entorno virtual e instalar dependencias:

```bash
pip install fastapi uvicorn sqlmodel psycopg2-binary sqlalchemy
```
2. Editar el archivo db.py y poner tu conexión:
DATABASE_URL = "postgresql+psycopg2://usuario:contraseña@localhost:5432/dbtest"

3. Levantar el servidor:
python -m uvicorn main:app --reload

4. Configuración del frontend
  a. ir a la carpeta forntend:
    cd frontend
    npm install
    npm start
  b. la app React estara en:
    http://localhost:3000

## 🗄️ Endpoints principales

POST /users/ → Crear usuario (nombre, email)
GET /users/ → Listar todos los usuarios
GET /users/{id} → Obtener usuario por

## 📂 Restaurar base de datos - PostgreSQL
  usar el archivo "dbtest.backup" y restaurar en Pgadmin4
