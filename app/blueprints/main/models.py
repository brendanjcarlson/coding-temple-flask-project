from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import requests

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


def poke_api():
    for i in range(1, 906):
        res_one = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(i)}')
        res_two = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{str(i)}')
        try:
            if res_one.ok and res_two.ok:
                data_one = res_one.json()
                data_two = res_two.json()
                new_pokemon = Pokemon(game_id=data_one["id"],name=data_one["name"],height=data_one["height"],weight=data_one["weight"],types=", ".join([t["type"]["name"] for t in data_one["types"]]),abilities=", ".join([a["ability"]["name"] for a in data_one["abilities"]]),sprite=data_one["sprites"]["front_default"],description=data_two["flavor_text_entries"][0]["flavor_text"])
                db.session.add(new_pokemon)
                db.session.commit()
        except:
            print("Error at request #", i)

poke_api()