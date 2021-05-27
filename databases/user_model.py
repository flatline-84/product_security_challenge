from .database import db
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pyotp

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

    totp_secret = db.Column(db.String(30), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.gen_hashed_password(password)
        self.email = email
        self.date_created = datetime.utcnow()

        self.totp_secret = pyotp.random_base32()
    
    def __repr__(self):
        return f'<User {self.username}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def gen_hashed_password(self, password):
        return generate_password_hash(password + config.salt)

    def verify_password(self, password):
        return check_password_hash(self.password, password+config.salt)

    def verify_totp(self, otp):
        return pyotp.TOTP(self.totp_secret).verify(otp)
    
    def get_totp_uri(self):
        if self.totp_secret:
            return pyotp.totp.TOTP(self.totp_secret).provisioning_uri(name=self.email, issuer_name='ZenChair')

    def update_last_login(self):
        self.last_login = datetime.utcnow()
        self.save()
    
    def update_ip_address(self, ip_addr):
        self.last_ip_login = ip_addr
        self.save()
    
def get_valid_user(email, password, otp):
    user = User.query.filter_by(email=email).first()
    if not user:
        return None
    if user.verify_password(password) and user.verify_totp(otp):
        return user
    else:
        return None
