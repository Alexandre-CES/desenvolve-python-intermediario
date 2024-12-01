from app import app
from flask import (
    redirect,
    url_for,
    request,
    render_template
)
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)
from app import alquimias

@app.route('/')
def index():
    user=None
    posts=[]
    if current_user.is_authenticated:
        user = current_user
        posts = alquimias.get_timeline()
    return render_template('index.html', title='Página inicial', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()

        user = alquimias.validate_user_password(username, password)
        if user:
            print('\nLogin bem sucedido!\n')
            login_user(user,remember=user.remember)
            return redirect(url_for(f'index'))
        else:
            print('\nUsuário ou senha inválidos\n')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():

    if request.method == 'POST':
        username = request.form['username'].lower()
        if alquimias.user_exists(username):
            print('\nUsuário já existe!\n')
            return redirect(url_for('login'))
        else:
            username = username
            password = request.form['password'].lower()
            confirm_password = request.form['confirm-password'].lower()

            if password != confirm_password:
                return redirect(url_for(f'cadastro'))

            remember = True if request.form.get('remember') == 'on' else False
            profile_picture = request.form.get('profile-picture')
            bio = request.form.get('bio')

            user = alquimias.create_user(username,password,remember,profile_picture,bio)
            login_user(user, remember=remember)
            
            return redirect(url_for(f'index'))
    else:
        return render_template('cadastro.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(f'index'))

@app.route('/post', methods=['GET','POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form.get('body')
        if body:
            alquimias.create_post(body)
            return redirect(url_for(f'index'))
        else:
            return redirect(url_for(f'post'))
    else:
        return render_template('post.html')