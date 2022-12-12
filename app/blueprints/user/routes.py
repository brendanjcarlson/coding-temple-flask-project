from . import bp as app
from flask import render_template, request, redirect, url_for, flash, session
from app import db
from app.blueprints.main.models import User, Pokemon, pokemon_user
from flask_login import current_user, login_required


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    pokemon = Pokemon.query.join(pokemon_user).filter_by(user_id=current_user.id).all()
    return render_template('profile.html.j2', user=current_user, pokemon=pokemon)

@app.route('/account/', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html.j2', user=current_user)


@app.route('/pick/<int:id>', methods=['POST'])
@login_required
def pick(id):
    pokemon = Pokemon.query.filter_by(game_id=id).first()
    try:
        statement = pokemon_user.insert().values(pokemon_id=id, user_id=current_user.id)
        db.session.execute(statement)
        db.session.commit()
        flash(f'Added {pokemon.name.title()} to your page!', 'success')
    except Exception as e:
        flash(f'Error picking {pokemon.name.title()}', 'danger')
    return redirect(url_for('user.profile'))