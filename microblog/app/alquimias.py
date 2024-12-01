from app import db
from sqlalchemy import select, desc
from app.models.models import User, Post
from datetime import datetime
from flask_login import current_user

def validate_user_password(username,password):
    res = db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    if user and user.password == password: return user
    else: return None

def user_exists(username):
    res = db.session.scalars(select(User).where(User.username == username))
    if res.first() : return res.first()
    else: return None

def create_user(username, password, remember=False,profile_picture=None,bio=None, last_login=None):
    new_user = User(
        username = username,
        password = password,
        remember = remember,
        profile_picture = profile_picture,
        bio = bio,
        last_login = last_login if last_login else datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()

    return new_user

def create_post(body):
    new_post = Post(
        user_id = current_user.id,
        body = body,
        timestamp = datetime.now()
    )
    db.session.add(new_post)
    db.session.commit()

def get_timeline():
    posts_db = (
        db.session.query(Post)
        .order_by(Post.timestamp.desc())
        .limit(5)
        .all()
    )
    posts = []
    for post in posts_db:
        posts.append({'author':post.author.username, 'body':post.body})
    return posts