from flask import Blueprint, render_template
from .models import Product
from flask_login import login_required

views = Blueprint('views',__name__)

@views.route('/')
def home():

    items = Product.query.all()
    for product in items:
        print(len(items),product.product_name, product.current_price, product.previous_price, product.product_picture, product.in_stock)
    for item in items:
        if item.product_picture:
            product_picture_path = item.product_picture.split('/')[1:]
            final_product_picture_path = '/'.join(product_picture_path)
            print(final_product_picture_path)
    return render_template('home.html', items=items)

@views.route('/add-to-cart/<int:item_id')
@login_required
def add_to_cart(item_id)
