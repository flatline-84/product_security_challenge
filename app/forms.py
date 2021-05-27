from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Passwords must match'),
        validators.Length(min=8, max=35)
    ])
    password_confirm = PasswordField('Repeat Password')

# Not used anymore
class Register2FAForm(Form):
    pass

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=35)
    ])
    otp = StringField('OTP', [validators.Length(min=6, max=6)])

class ResetPasswordForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=35)
    ])
    new_password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('new_password_confirm', message='Passwords must match'),
        validators.Length(min=8, max=35)
    ])
    new_password_confirm = PasswordField('Repeat Password')
    otp = StringField('OTP', [validators.Length(min=6, max=6)])