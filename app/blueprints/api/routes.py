from . import bp as app
from app.blueprints.main.models import User
from app import db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
import re


@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form['search']
        try:
            if isinstance(int(search), int):
                pokemon = Pokemon.query.filter_by(game_id=search).first()
            else:
                pokemon = Pokemon.query.starts_with(search).all()
            render_template('search.html.j2',
                            user=current_user, pokemon=pokemon)
        except Exception as e:
            return render_template('search.html.j2', user=current_user, pokemon=pokemon, error=e)
