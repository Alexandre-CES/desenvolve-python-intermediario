from app import login
from flask_login import UserMixin

class User(UserMixin, db.model):
    __tablename__='users'

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))