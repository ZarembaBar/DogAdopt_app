from app import app, db
from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required, logout_user, login_user
from app.forms import LoginForm, NewUserForm
from app.models import User
from urllib.parse import urlsplit


@app.route('/')
@app.route('/index')
# @login_required
def index():
    return render_template('start_page.html', title='DogAdopt')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(user_email=login_form.email.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Błędna nazwa użytkownika/hasło')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)
    return render_template('login.html', login_form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    new_user_form = NewUserForm()
    if new_user_form.validate_on_submit():
        user = User(user_name=new_user_form.user_name.data, user_surname=new_user_form.user_surname.data, user_email=new_user_form.user_email.data)
        user.set_password(new_user_form.user_password.data)
        db.session.add(user)
        db.session.commit()
        flash('Pomyślnie dodano nowego użytkownika')
        return redirect(url_for('login'))
    return render_template('register.html', new_user_form=new_user_form)