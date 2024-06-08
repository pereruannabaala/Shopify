from flask import Blueprint, render_template
from .models import Product


views = Blueprint('views',__name__)

@views.route('/')
def home():

    items = Product.query.all()
    for product in items:
        print(len(items),product.product_name, product.current_price, product.previous_price, product.product_picture, product.in_stock)
    return render_template('home.html', items=items)
