from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True)
    phone = db.Column(db.Integer, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Book:
    def __init__(self):
        pass

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bookName = db.Column(db.String(120), index=True, unique=True, nullable=True)
    image = db.Column(db.String(120), index=True, unique=True, nullable=True)
    description = db.Column(db.String(120), index=True, unique=True, nullable=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))


class Genre:
    def __init__(self):
        pass

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(120), index=True, unique=True, nullable=True)
    genre = db.Column(db.String(120), index=True, unique=True, nullable=True)
    book_id = db.relationship('Address', backref='person', lazy=True)


class Library:
    def __init__(self):
        pass

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        #userID integer NOT NULL,
        #bookID integer NOT NULL


class Rate:
    def __init__(self):
        pass

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rate = db.Column(db.String(120), index=True, unique=True, nullable=True)
    comment = db.Column(db.String(120), index=True, unique=True, nullable=True)
    book_id = db.relationship('Address', backref='person', lazy=True)
    user_id = db.relationship('Address', backref='person', lazy=True)


