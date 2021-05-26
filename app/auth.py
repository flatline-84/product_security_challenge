from flask import Blueprint, request, render_template, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Check user here
        # return redirect(url_for('success',name = user))
        pass
    if request.method == 'GET':
        flash("flash message")
        return render_template('auth/login.html')

@auth.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        flash(username)
        flash(password) #sEkUriTy
        return render_template('auth/register.html')

@auth.route('/logout', methods = ['POST'])
def logout():
    pass