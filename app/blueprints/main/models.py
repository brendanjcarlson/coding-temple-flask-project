from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # todo: add a character avatar
    # todo: add a bio
    # todo: add a

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer)
    name = db.Column(db.String(128))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    types = db.Column(db.String(128))
    abilities = db.Column(db.String(128))
    sprite = db.Column(db.String(128))
    description = db.Column(db.String(512))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


pokemon_user = db.Table('pokemon_user',
                        db.Column('user_id', db.Integer, db.ForeignKey(
                            'user.id'), primary_key=True),
                        db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True))
