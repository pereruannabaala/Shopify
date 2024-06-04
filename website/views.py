from flask import Blueprint, render_template
from .models import Product


views = Blueprint('views',__name__)

@views.route('/')
def home():

    items = Product.query.filter_by(flash_sale=True)
    return render_template('home.html', items=items)