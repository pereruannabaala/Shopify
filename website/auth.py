from flask import Blueprint, render_template
from .forms import LoginForm, SignUpForm
from .models import Customer

auth = Blueprint('auth', __name__)



@auth.route('/signup', methods='GET','POST')
def sign_up(): 
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 == password2:

    return render_template('signup.html', form=form)



@auth.route('/login', methods='GET','POST')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

