from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

app.config.from_object('config.Config')

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)


from app.blueprints.main import bp as main_bp
app.register_blueprint(blueprint=main_bp)

from app.blueprints.page import bp as page_bp
app.register_blueprint(blueprint=page_bp)

from app.blueprints.api import bp as api_bp
app.register_blueprint(blueprint=api_bp)

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(blueprint=auth_bp)
