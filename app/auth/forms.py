# from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField,BooleanField
# from wtforms.validators import Required,Email,EqualTo
# from ..models import User
# from wtforms import ValidationError

# class RegistrationForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[Required(),Email()])
#     username = StringField('Enter your username',validators = [Required()])
#     password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
#     password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
#     submit = SubmitField('Sign Up')

# class LoginForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[Required(),Email()])
#     password = PasswordField('Password',validators =[Required()])
#     remember = BooleanField('Remember me')
#     submit = SubmitField('Sign In')

# def validate_email(self,data_field):
#     if User.query.filter_by(email =data_field.data).first():
#         raise ValidationError('There is an account with that email')

# def validate_username(self,data_field):
#     if User.query.filter_by(username = data_field.data).first():
#         raise ValidationError('That username is taken')

"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional
)


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')