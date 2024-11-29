from app import db
from sqlalchemy import select
from app.models.models import User
from datetime import datetime

def validate_user_password(username,password):
    res = db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    if user and user.password == password: return user
    else: return None

def user_exists(username):
    res = db.session.scalars(select(User).where(User.username == username))
    if res.first() : return res.first()
    else: return None

def create_user(username, password, remember=False, last_login=None):
    new_user = User(
        username = username,
        password = password,
        remember = remember,
        last_login = last_login if last_login else datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()

    return new_user