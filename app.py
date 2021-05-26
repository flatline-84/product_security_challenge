# Imports
from flask import Flask
from flask import redirect, url_for, request, render_template, flash
# Custom Imports
from config import Config #contains configuration for webapp
from app.auth import auth


# Create our main application here
app = Flask(__name__)
config = Config()

@app.route('/')
def index():
    # if authed:
    # return render_template('home.html')
    # if unauthed:
    return render_template('main.html')


if __name__ == "__main__":
    # Setup up application
    app.secret_key = config.secret_key
    # Register routes via blueprints
    app.register_blueprint(auth)
    # Begin running the webapp
    app.run(config.hostname, config.port, config.debug)