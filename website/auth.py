from flask import Blueprint, render_template
from .forms import LoginForm, SignUpForm


auth = Blueprint('auth', __name__)


@auth.route('/sign-up')
def sign_up(): 
    form = SignUpForm()

    return render_template('sign-up.html', form=form)



@auth.route('/login')
def login():
    return 'This is the login page'

