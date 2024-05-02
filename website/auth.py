from flask import Blueprint, render_template, flash, redirect
from .forms import LoginForm, SignUpForm
from .models import Customer
from . import db

auth = Blueprint('auth', __name__)




@auth.route('/signup', methods=['GET', 'POST'])
def sign_up(): 
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 == password2:
            new_customer = Customer()
            new_customer.email = email
            new_customer.username = username
            new_customer.password = password2

        try:
            db.session.add(new_customer)
            db.session.commit()
            flash('Account Created Successfully, You can now Login')
            return redirect('/login')
        except Exception as e:
            print(e)
            flash('Account not created! Email already exists')

        form.email.data = ''
        form.username.data = ''
        form.password1.data = ''
        form.password2.data = ''

    return render_template('signup.html', form=form)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
    return render_template('login.html', form=form)

