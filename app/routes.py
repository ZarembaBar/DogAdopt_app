from app import app, db
from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required, logout_user, login_user
from app.forms import LoginForm, NewDogForm, NewUserForm
from app.models import Dog, User
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
    form = NewUserForm()
    if form.validate_on_submit():
        user = User(user_name=form.user_name.data,
                    user_surname=form.user_surname.data,
                    user_email=form.user_email.data)
        user.set_password(form.user_password.data)
        db.session.add(user)
        db.session.commit()
        flash('Pomyślnie dodano nowego użytkownika')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/user/<id>', methods=['GET', 'POST'])
def user(id):
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('user_account_display.html', user=user)


@app.route('/dog_account', methods=['GET', 'POST'])
def create_dog_account():
    form = NewDogForm()
    if form.validate_on_submit():
        dog = Dog(name=form.name.data,
                  breed=form.breed.data,
                  location=form.location.data,
                  description=form.description.data,
                  owner_id=current_user.id)
        db.session.add(dog)
        db.session.commit()
        flash(f'Dodano konto psa {dog.name} do adopcji')
        return redirect(url_for('index'))
    return render_template('new_dog_account.html', form=form)
