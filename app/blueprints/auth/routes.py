from . import bp as app
from app.blueprints.main.models import User
from app import db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html.j2', title='Sign Up')

    username = request.form['username'].strip()
    email = request.form['email'].strip()
    first_name = request.form['firstName'].strip()
    last_name = request.form['lastName'].strip()
    password = request.form['password'].strip()
    confirm_password = request.form['confirmPassword'].strip()

    username_exists = User.query.filter_by(username=username).first()
    email_exists = User.query.filter_by(email=email).first()

    if user_exists is not None or email_exists is not None or password != confirm_password:
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


@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html.j2', title='Sign In')

    email = request.form['email']
    password = request.form['password']
    next_url = request.form['next_url']

    user = User.query.filter_by(email=email).first()

    if user is None:
        flash(message=f'No user with email {email} found.', category='danger')
    elif user.check_password_hash(password):
        login_user(user)
        flash(message=f'Login successful. Welcome back {user.username}', category='success')
        if next_url:
            return redirect(next_url)
        return redirect(url_for('main.home'))
    else:
        flash(message=f'Invalid credentials.', category='danger')

    return render_template('login.html.j2', title='Login')

@app.route('/logout')
def logout():
    logout_user()
    flash(message='Logout successful.', category='success')
    return redirect(url_for('main.home'))


## REDIRECTS
@app.route('/login')
def login():
    return redirect(url_for('auth.sign_in'))

@app.route('/register')
def register():
    return redirect(url_for('auth.sign_up'))