"""Signup & login forms."""
from wtforms import (Form,
                     StringField,
                     PasswordField,
                     SubmitField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                Optional)


class SignupForm(Form):
    """User Signup Form."""

    name = StringField('Name',
                       validators=[DataRequired(message='Enter your name.')])
    email = StringField('Email',
                        validators=[Length(min=6, message='Enter a valid email address.'),
                                    Email(message='Enter a valid email address.'),
                                    DataRequired(message='Enter an email address.')])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Enter a password.'),
                                         Length(min=6, message='Select a stronger password.'),
                                         EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Your Password',)
    website = StringField('Website',
                          validators=[Optional()])
    submit = SubmitField('Register')


class LoginForm(Form):
    """User Login Form."""

    email = StringField('Email', validators=[DataRequired('Provide your account\'s email address.'),
                                             Email('Enter a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired('Enter your password.')])
    submit = SubmitField('Log In')
