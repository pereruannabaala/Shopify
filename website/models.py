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

    
    class Product(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        product_name = db.Column(db.String(100), nullable=False)
        current_price = db.Column(db.Float, nullable=False)
        previuos_price = db.Column(db.Float, nullable=False)
        in_stock = db.Column(db.Integer, nullable=False)
        product_picture = db.Column(db.String(1000), nullable=False)
        flash_sale = db.Column(db.Boolean, default=False)
        date_added = db.Column(db.DateTime(), default=datetime.utcnow)

        def __str__(self):
            return 'Product &r>' % Product.id # prints(Product1) <Product 1>

    
    class Cart(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        quantity = db.Column(db.Integer, nullable=False)
    
    def __str__(self):
        return 'Cart &r>' % Cart.id # prints(Cart1) <Cart 1>