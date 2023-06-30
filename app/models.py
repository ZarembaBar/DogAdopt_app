from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users_table'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), index=True)
    user_surname = db.Column(db.String(50), index=True)
    user_email = db.Column(db.String(50), index=True, unique=True)
    user_password_hash = db.Column(db.String(150))

    def __repr__(self):
        return '<Użytkownik {}>'.format(self.user_name)

    def set_password(self, password):
        self.user_password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_password_hash, password)


class Dog(db.Model):
    __tablename__ = 'dogs_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    breed = db.Column(db.String(50))
    location = db.Column(db.String(50))
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    owner = db.relationship('User')

    def __repr__(self):
        return '<Piesek {}>'.format(self.name)
