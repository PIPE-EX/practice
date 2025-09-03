from sqlmodel import create_engine, Session

# Reemplaza con tu propia conexión
DATABASE_URL = "postgresql+psycopg2://postgres:plantera6@localhost:5432/dbtest"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session