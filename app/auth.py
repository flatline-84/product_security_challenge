from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from databases.database import db
from databases.user_model import User

from app.forms import RegistrationForm

auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Check user here
        # return redirect(url_for('success',name = user))
        pass
    if request.method == 'GET':
        flash("flash message")
        return render_template('auth/login.html')

@auth_blueprint.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    # form.validate() returns true if all validation checks on data pass
    if request.method == 'POST' and form.validate():

        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            user = User(form.username.data, form.password.data, form.email.data)
            db.session.add(user)
            db.session.commit()
            session['logged_in'] = True
            session['username'] = form.username.data
            
            flash("Your registration is complete!")
        else:
            # TODO: work out how not to perform email enumeration
            flash("Email is already connected to an account!")
        return redirect(url_for('main_blueprint.index'))
    
    return render_template('auth/register.html', form=form)

@auth_blueprint.route('/logout', methods = ['POST'])
def logout():
    pass