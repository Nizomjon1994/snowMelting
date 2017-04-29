from flask_wtf import Form, validators
from wtforms import TextField, PasswordField, BooleanField, StringField


class RegistrationForm(Form):
    username = StringField('Username')
    email = StringField('Email Address')
    password = PasswordField('New Password'
                             )

    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
                              )
