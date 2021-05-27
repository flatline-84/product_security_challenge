from flask import Blueprint, request, render_template, flash

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
    if request.method == 'GET':
        return render_template('auth/register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        flash(username)
        flash(password) #sEkUriTy
        return render_template('auth/register.html')

@auth_blueprint.route('/logout', methods = ['POST'])
def logout():
    pass