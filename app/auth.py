from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from databases.database import db
from databases.user_model import User, get_valid_user

from app.forms import RegistrationForm, Register2FAForm, LoginForm

auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = get_valid_user(form.email.data, form.password.data, form.otp.data)
        if not user:
            flash("Email or password is incorrect. Please try again")
            return redirect(url_for('auth_blueprint.login'))
        else:
            flash("Logged in successfully!")
            login_user(user, request)
        return redirect(url_for('main_blueprint.index'))

    return render_template('auth/login.html', form=form)


@auth_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    # form.validate() returns true if all validation checks on data pass
    if request.method == 'POST' and form.validate():

        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            # Create the user and put them in the database
            user = User(form.username.data,
                        form.password.data, form.email.data)

            try:
                db.session.add(user)
                db.session.commit()
                # Update our session and log our user in
                login_user(user, request)
                session['2fa'] = user.get_totp_uri()
                session.modified = True
                flash("Your initial registration is complete!")
            except Exception as error:
                db.session.rollback()
                flash("Error occured. Account could not be created!")
                # flash("Error occured! " + error['orig'])
                # print("Erroring!!!")
                # print(error.__dict__)
        else:
            # TODO: work out how not to perform email enumeration
            flash("Email is already connected to an account!")
        return redirect(url_for('auth_blueprint.register_2fa'))

    return render_template('auth/register.html', form=form)

@auth_blueprint.route('/register/2fa', methods=['GET'])
def register_2fa():
    if '2fa' in session:
        return render_template('auth/register_twofactor.html')
    else:
        return redirect(url_for('main_blueprint.index'))

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('main_blueprint.index'))

@auth_blueprint.route('/change-password', methods=['GET', 'POST'])
def change_password():
    pass

def login_user(user, request):
    session['logged_in'] = True
    session['username'] = user.username
    session['last_login'] = user.last_login
    session['last_ip_login'] = user.last_ip_login

    # if user.totp_secret == "dummy":
    #     session['2fa_verified'] = False
    # else:
    #     session['2fa_verified'] = True

    session.modified = True

    user.update_last_login()
    user.update_ip_address(request.remote_addr)

def logout_user():
    # Set our logged in session to false
    session['logged_in'] = False

    # Remove all user specific session variables
    session.pop('username', None)
    session.pop('last_login', None)
    session.pop('last_ip_login', None)
    session.pop('2fa', None)

    session.modified = True
