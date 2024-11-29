
def validate_user_password(username,password):

    user = res.first()
    if user and user.password == password: return user
    else: return None

def user_exists(username):

    user = res.first()
    return user

def create_user(username, password, remember=False, last_login=None):

    return new_user
