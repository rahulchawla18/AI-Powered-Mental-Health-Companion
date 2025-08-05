from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models.models import User
from backend.database.database import get_db

def login_user(username: str, db: Session = Depends(get_db)):
    ...
    user = db.query(User).filter(User.username == username).first()
    if not user:
        user = User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)