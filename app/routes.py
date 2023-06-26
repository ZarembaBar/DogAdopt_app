from app import app
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required, logout_user
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('start_page.html', title='DogAdopt')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Błędna nazwa użytkownika/hasło')
            return redirect(url_for('login'))
    return render_template('login.html', login_form=login_form)


@app.route('/logout')
def logout_user():
    logout_user()
    return redirect(url_for('index'))
