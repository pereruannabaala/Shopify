from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
    
class SignUpForm(FlaskForm):
    email = EmailField('Enter Your Email', validators=[DataRequired()])
    username = StringField('Enter Your Username', validators=[DataRequired(), Length(min=2)])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Your Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Enter Your Email', validators=[DataRequired()])
    password = PasswordField('Enter Your Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), Length(min=6)])
    change_password = SubmitField('Change Password')
