from flask import Blueprint, request, render_template, flash, session

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def index():
    if 'logged_in' not in session:
        session['logged_in'] = False
    elif session['logged_in'] is True:
        return render_template('home.html')
        
    return render_template('main.html')