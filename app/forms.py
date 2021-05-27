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

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=35)
    ])
