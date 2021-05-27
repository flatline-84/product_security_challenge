from flask import Blueprint, request, render_template, flash

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def index():
    # if authed:
    # return render_template('home.html')
    # if unauthed:
    return render_template('main.html')