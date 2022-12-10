from . import bp as app
from app.blueprints.main.models import User
from app import db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
import re

## determining if login is by email or username
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@')
def isEmail(email):
    return True if regex.match(email) else False

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html.j2')

    first_name = request.form['firstName']
    last_name = request.form['lastName']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']

    username_exists = User.query.filter_by(username=username).first()
    email_exists = User.query.filter_by(email=email).first()

    if username_exists is not None or email_exists is not None or password != confirm_password:
        if user_exists is not None:
            flash(f'User with username {username} already exists.', category='danger')
        if email_exists is not None:
            flash(f'User with email {email} already exists.', category='danger')
        if password != confirm_password:
            flash(f'Passwords do not match.', category='danger')
    else:
        try:
            new_user = User(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            new_user.hash_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Welcome to PokéPicker, {username}! Please log in.', category='success')
            return redirect(url_for('auth.login'))
        except:
            flash(f'Something went wrong. Please try again.', category='danger')
    return render_template('login.html.j2')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html.j2')

    identifier = request.form['identifier']
    password = request.form['password']
    # next_url = request.form['next_url']

    if isEmail(identifier):
        user = User.query.filter_by(email=identifier).first()
    else:
        user = User.query.filter_by(username=identifier).first()


    if user is None:
        flash(message=f'No user with email {identifier} found.', category='danger')
    elif user.check_password(password):
        login_user(user)
        flash(message=f'Login successful.', category='success')
        # if next_url:
        #     return redirect(next_url)
        return redirect(url_for('main.home'))
    else:
        flash(message=f'Invalid credentials.', category='danger')

    return redirect(url_for('main.home'))

@app.route('/logout')
def logout():
    logout_user()
    flash(message='Logout successful.', category='success')
    return redirect(url_for('main.home'))