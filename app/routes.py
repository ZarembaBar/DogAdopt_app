from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('start_page.html', title='DogAdopt')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Zalogowano użytkownika {}'.format(login_form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', login_form=login_form)
