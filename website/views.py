from flask import Blueprint, render_template,flash,redirect,request,jsonify
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


@views.route('/cart')
@login_required
def show_cart():
    cart = Cart.query.filter_by(customer_link=current_user.id).all()
    amount = 0
    for item in cart:
        amount += item.product.current_price + item.quantity
    return render_template('cart.html', cart=cart, amount=amount, total=amount+200)


@views.route('/pluscart')
@login_required
def plus_cart():
    if request.method == 'GET':
        cart_id = request.args.get('cart_id')
        cart_item = Cart.query.get(cart_id)
        cart_item.quantity = cart_item.quantity + 1
        db.session.commit()
        
        cart = Cart.query.filter_by(customer_link=curremt_user.id).all()

        amount = 0

        for item in cart:
            amount += item.product.current_price * item.quantity

        data = {
            'quantity': cart_item.quantity,
            'amount': amount,
            'total': amount + 200
                }
        
        return jsonify(data)