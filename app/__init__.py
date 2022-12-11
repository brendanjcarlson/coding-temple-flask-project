import requests
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)


from app.blueprints.main import bp as main_bp
app.register_blueprint(blueprint=main_bp)

from app.blueprints.user import bp as user_bp
app.register_blueprint(blueprint=user_bp)

from app.blueprints.api import bp as api_bp
app.register_blueprint(blueprint=api_bp)

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(blueprint=auth_bp)


login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'danger'
