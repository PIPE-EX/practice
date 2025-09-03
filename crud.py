from sqlmodel import Session, select
from models import User, UserCreate

def create_user(session: Session, user: UserCreate) -> User:
    db_user = User(name=user.name, email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_users(session: Session):
    return session.exec(select(User)).all()

def get_user_by_id(session: Session, user_id: int):
    return session.get(User, user_id)