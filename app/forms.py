from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, PasswordField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')


class NewUserForm(FlaskForm):
    user_name = StringField('Imię', validators=[DataRequired()])
    user_surname = StringField('Nazwisko', validators=[DataRequired()])
    user_email = StringField('email', validators=[DataRequired(), Email(message='Błędny adres email')])
    user_password = PasswordField('hasło', validators=[DataRequired()])
    user_password_2 = PasswordField('powtórz hasło', validators=[DataRequired(), EqualTo('user_password',
                                                                                         message='Podane hasła nie są identyczne')])
    submit = SubmitField('Stwórz konto')

    def validate_user_email(self, user_email):
        user = User.query.filter_by(user_email=user_email.data).first()
        if user is not None:
            raise ValidationError('Podany email został już wcześniej użyty')


class NewDogForm(FlaskForm):
    name = StringField('Imie', validators=[DataRequired()])
    age = IntegerField('Wiek', validators=[DataRequired()])
    weight = SelectField('Waga', choices=[('small_dog', 'Mały 1-10kg'), ('medium_dog', 'Średni 11-20kg'),
                                          ('big_dog', 'Duży 20kg<')])
    breed = StringField('Rasa', validators=[DataRequired()])
    location = StringField('Lokalizacja', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    photo = FileField()
    submit = SubmitField('Dodaj')
