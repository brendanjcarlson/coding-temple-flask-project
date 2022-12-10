from . import bp as app
from flask import render_template, request, redirect, url_for, flash, session
from app import db
from app.blueprints.main.models import User, Pokemon
from flask_login import current_user, login_required


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html.j2', title='Home', user=current_user)