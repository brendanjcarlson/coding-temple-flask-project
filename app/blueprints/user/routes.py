from . import bp as app
from flask import render_template, request, redirect, url_for, flash, session
from app import db
from app.blueprints.main.models import User, Pokemon
from flask_login import current_user, login_required


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html.j2', user=current_user)

@app.route('/account/', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html.j2', user=current_user)