#####################################
#       Project: ZenChair           #
#       Author: Peter K             #
#       Date Started: 26/05/2021    #
#       Date Completed:             #
#####################################

# Imports
from flask import Flask
from flask import redirect, url_for, request, render_template, flash
from flask_wtf.csrf import CSRFProtect
# For database and models
from flask_sqlalchemy import SQLAlchemy
from databases.database import db
# Custom Imports
from config import Config #contains configuration for webapp
from app.auth import auth_blueprint
from app.routes import main_blueprint
from app.security import SecurityHardening

config = Config()
csrf = CSRFProtect()

def create_app():
    # Create our main application here
    app = Flask(__name__)
    # Get the database
    app.config['SQLALCHEMY_DATABASE_URI'] = config.db_conn_string 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = config.secret_key
    # Create the database connection
    db.init_app(app)
    # initialize CSRF protection from flask-wtf
    csrf.init_app(app)

    # Register routes via blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    # Register the security middleware that provides hardening
    app.wsgi_app = SecurityHardening(app.wsgi_app)

    # Load our models into the database
    from databases.user_model import User
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    # Begin running the webapp
    app.run(config.hostname, config.port, config.debug)