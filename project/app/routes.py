from flask import Blueprint, request, render_template, flash, session

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def index():
    # User trying to be cheeky and avoid setting up 2FA
    # if '2fa_verified' in session and session['2fa_verified'] == False:
    #     return redirect(url_for('auth_blueprint.register_2fa'))
    
    # Fresh user, we don't care though
    if 'logged_in' not in session:
        session['logged_in'] = False
    # If the user is logged in, send them home
    elif session['logged_in'] is True:
        return render_template('home.html')
        
    return render_template('main.html')