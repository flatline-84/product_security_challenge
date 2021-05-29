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
import logging
# For database and models
from flask_sqlalchemy import SQLAlchemy
from databases.database import db
# Custom Imports
from config import Config #contains configuration for webapp
from app.auth import auth_blueprint
from app.routes import main_blueprint
from app.security import SecurityHardening

# Load our config
config = Config()
# Initialize CSRF protection
csrf = CSRFProtect()

# Set our logging up
logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
handler = logging.FileHandler(config.log_file) # creates handler for the log file
logger.addHandler(handler) # adds handler to the werkzeug WSGI logger so we get both console and file loggingapp.logger

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

    # Make flask session cookies secure
    app.config['SESSION_COOKIE_SECURE'] = True

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
    app.run(
        config.hostname, 
        config.port, 
        config.debug, 
        ssl_context='adhoc')