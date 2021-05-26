## Imports
from flask import Flask
from flask import redirect, url_for, request, render_template, flash
from config import Config

# Create our main application here
app = Flask(__name__, template_folder='app/templates')
config = Config()

@app.route('/')
def main_page():
    # if unauthed:
    return render_template('home.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Check user here
        # return redirect(url_for('success',name = user))
        pass
    if request.method == 'GET':
        flash("flash message")
        return render_template('auth/login.html')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    pass

@app.route('/logout', methods = ['POST'])
def logout():
    pass

if __name__ == "__main__":
    app.secret_key = config.secret_key
    app.run(config.hostname, config.port, config.debug)