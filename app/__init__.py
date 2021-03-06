from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth_bp.login'

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations

    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    from .auth import auth_bp as auth_bp_blueprint
    # app.register_blueprint(main_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_bp_blueprint)

    return app