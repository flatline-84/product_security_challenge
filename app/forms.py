from wtforms import Form, BooleanField, StringField, PasswordField, validators, ValidationError
import re


def validate_password_complexity(form, field):
    password = field.data
    # Min 8 chars, one upper, one lower, one number, one special char
    # could have done this manually but a single regex is so much easier
    regex_string = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'

    check_password = re.findall(regex_string, password)
    if not check_password:
        raise ValidationError(
            'Password must contain min 8 chars, one upper char, one lower char, one number, and one special char')


class RegistrationForm(Form):
    username = StringField(
        'Username',
        [validators.Length(min=4, max=25)],
        render_kw={"placeholder":"flatline-84"}
    )
    email = StringField(
        'Email Address',
        [validators.Length(min=6, max=35), validators.Email()],
        render_kw={"placeholder": "xx_1337_guy_xx@zenchair.com"}
    )

    password = PasswordField(
        'New Password', [
            validators.DataRequired(),
            validators.EqualTo('password_confirm',
                            message='Passwords must match'),
            validators.Length(min=8, max=32),
            validate_password_complexity
        ])
    password_confirm = PasswordField('Repeat Password')

# Not used anymore


class Register2FAForm(Form):
    pass


class LoginForm(Form):
    email = StringField(
        'Email Address',
        [validators.Length(min=6, max=35), validators.Email()]
    )
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=35)
    ])
    otp = StringField('OTP', [validators.Length(min=6, max=6)])


class ResetPasswordForm(Form):
    email = StringField(
        'Email Address',
        [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField(
        'Password', [
            validators.DataRequired(),
            validators.Length(min=8, max=32),
            validate_password_complexity
        ])
    new_password = PasswordField(
        'New Password', [
            validators.DataRequired(),
            validators.EqualTo('new_password_confirm',
                            message='Passwords must match'),
            validators.Length(min=8, max=32)
        ])
    new_password_confirm = PasswordField('Repeat Password')
    otp = StringField(
        'OTP', 
        [validators.Length(min=6, max=6)],
        render_kw={"maxlength": "6"})
