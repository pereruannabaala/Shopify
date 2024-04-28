from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1oo),unique=True)
    username = db.Column(db.String(100),nullable=False)
    password_hash= db.Column(db.String(150),nullable=False)
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)

# password_hash decorator 
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute ')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password=password)
    
    def __str__(self):
        return 'Customer &r>' % Customer.id # prints(Customer1) <Customer 1>

    