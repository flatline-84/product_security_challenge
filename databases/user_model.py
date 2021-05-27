from .database import db
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

config = Config()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(240), nullable=False)
    date_created = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    last_ip_login = db.Column(db.String(30))

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password + config.salt)
        self.email = email
        self.date_created = datetime.now()
    
    def __repr__(self):
        return f'<User {self.username}>'

    def verify_password(self, password):
        return check_password_hash(self.password, password+config.salt)
    
def get_valid_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return None
    if user.verify_password(password):
        return user
    else:
        return None
