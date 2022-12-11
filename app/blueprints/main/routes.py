from . import bp as app
from flask import render_template, request, redirect, url_for, flash, session
from app import db
from app.blueprints.main.models import User, Pokemon
from flask_login import current_user, login_required


@app.route('/', methods=['GET', 'POST'])
def home():
    pokemon = [Pokemon.query.filter_by(game_id=1).first(), Pokemon.query.filter_by(
        game_id=4).first(), Pokemon.query.filter_by(game_id=7).first()]
    return render_template('home.html.j2', user=current_user, pokemon=pokemon)
