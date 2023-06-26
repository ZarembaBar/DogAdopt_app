from app import db


class User(db.Model):
    __tablename__ = 'users_table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(150))

    def __repr__(self):
        return '<Użytkownik {}>'.format(self.username)


class Dog(db.Model):
    __tablename__ = 'dogs_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    breed = db.Column(db.String(50))
    location = db.Column(db.String(50))
    description = db.Column(db.Text)
    owner = db.Column(db.Integer, db.ForeignKey('users_table.id'))

    def __repr__(self):
        return '<Piesek {}>'.format(self.name)
