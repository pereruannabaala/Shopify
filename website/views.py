from flask import Blueprint, render_template,flash,redirect,request
from .models import Product, Cart
from flask_login import login_required, current_user
from . import db 


views = Blueprint('views',__name__)

@views.route('/')
def home():
    items = Product.query.all()
    for product in items:
        if product.product_picture:
            print('------->', 
                len(items),
                product.product_name,
                product.current_price,
                product.previous_price,
                product.product_picture,
                product.in_stock)
    for item in items:
        if item.product_picture:
            product_picture_path = item.product_picture.split('/')[3:]
            final_product_picture_path = '/'.join(product_picture_path)
            print("Product path", final_product_picture_path)
    return render_template('home.html', items=items, cart = Cart.query.filter_by(customer_link=current_user.id).all()
                            if current_user.is_authenticated else [] )


@views.route('/add-to-cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    item_to_add = Product.query.get(item_id)
    item_exists = Cart.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
    if item_exists:
        try:
            item_exists.quantity = item_exists.quantity + 1 
            db.session.commit()
            flash(f' Quantity of { item_exists.product.product_name } has been updated')
            return redirect(request.referrer)
        except Exception as e:
            print('Quantity not Updated', e)
            flash(f'Quantity of { item_exists.product.product_name } not updated')
            return redirect(request.referrer)
        except Exception as e:
            print('Quantity not Updated', e)
            flash(f'Quantity of { item_exists.product.product_name} not updated')
            return redirect(request.referrer)

    new_cart_item = Cart(
        quantity = 1,
        product_link = item_to_add.id,
        customer_link = current_user.id,
    )

    try:
        db.session.add(new_cart_item)
        db.session.commit()
        flash(f'{new_cart_item.product.product_name} added to cart')
    except Exception as e:
        print('Item not added to Cart',e)
        flash(f'{new_cart_item.product.product_name} has not been added to Cart')
    return redirect(request.referrer)


@Views.route('/cart')
@login_required
def show_cart():
    