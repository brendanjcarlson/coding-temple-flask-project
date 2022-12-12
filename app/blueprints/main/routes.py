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


@app.route('/search/', methods=['GET', 'POST'])
@login_required
def search():
    name = request.form['name']
    print(name)
    pokemon = Pokemon.query.filter_by(name=name).first()
    return render_template('single.html.j2', user=current_user, pokemon=pokemon)


@app.route('/pokemon/<int:game_id>', methods=['GET', 'POST'])
@login_required
def pokemon(game_id):
    pokemon = Pokemon.query.filter_by(game_id=game_id).first()
    return render_template('single.html.j2', user=current_user, pokemon=pokemon)