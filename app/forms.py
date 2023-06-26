from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')


class NewUserForm(FlaskForm):
    user_name = StringField('Imię', validators=[DataRequired()])
    user_surname = StringField('Nazwisko', validators=[DataRequired()])
    user_email = StringField('email', validators=[DataRequired()])
    user_password = PasswordField('hasło', validators=[DataRequired()])
    submit = SubmitField('Akceptuj')
