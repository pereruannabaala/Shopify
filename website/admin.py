from flask import Blueprint, render_template, flash, send_from_directory, url_for, redirect
from flask_login import login_required, current_user
from .forms import ShopItemsForm, OrderForm
from .models import Product, Order
from . import db
from werkzeug.utils import secure_filename
import os
from . import app

admin = Blueprint('admin',__name__)

@admin.route('/static/<path:filename>')
def get_image(filename):
    return send_from_directory('../static', filename)



#add items forms
@admin.route('/add-shop-items', methods=['GET','POST'])
@login_required
def add_shop_items():
    if current_user.id == 1:
        form = ShopItemsForm()
        if form.validate_on_submit():
            product_name = form.product_name.data 
            current_price = form.current_price.data
            previous_price = form.previous_price.data
            in_stock = form.in_stock.data
            flash_sale = form.flash_sale.data

            file = form.product_picture.data

            file_name = secure_filename(file.filename)# removes whitespace and invalid characters from filename
            
            file_path = os.path.join('website/static/images/' + file_name)


            file.save(file_path)

            new_shop_item = Product()
            new_shop_item.product_name = product_name
            new_shop_item.current_price = current_price
            new_shop_item.previous_price = previous_price
            new_shop_item.in_stock = in_stock
            new_shop_item.flash_sale = flash_sale

            new_shop_item.product_picture = file_path

            try:
                db.session.add(new_shop_item)
                db.session.commit()
                flash(f'{product_name} added successfully')
                print('Product Added')
                return render_template('add-shop-items.html', form=form)
            except Exception as e:
                print(e)
                flash('Item Not added')

        return render_template('add-shop-items.html',form=form)
    return render_template('404.html')


@admin.route('/shop-items', methods=['GET', 'POST'])
@login_required
def shop_items():
    if current_user.id == 1:
        items = Product.query.order_by(Product.date_added).all()
        for item in items:
            if item.product_picture:
                product_picture_path = item.product_picture.split('/')[1:]
                final_product_picture_path = '/'.join(product_picture_path)
                print("Product path (admin)---->",final_product_picture_path)
        return render_template('shop-items.html', items=items)
    return render_template('404.html')



@admin.route('/item-update/<int:item_id>', methods=['GET', 'POST'])
@login_required
def item_update(item_id):
    if current_user.id == 1:
        item = Product.query.get_or_404(item_id)
        form = ShopItemsForm()

#Add placeholders for UpdateItems
        item_to_update = Product.query.get(item_id)

        form.product_name.render_kw = { 'placeholder':  item_to_update.product_name}
        form.previous_price.render_kw = { 'placeholder': item_to_update.previous_price}
        form.current_price.render_kw = { 'placeholder': item_to_update.current_price}
        form.in_stock.render_kw = { 'placeholder': item_to_update.in_stock}
        form.flash_sale.render_kw = { 'placeholder': item_to_update.flash_sale}
        
        if form.validate_on_submit():
            product_name = form.product_name.data 
            current_price = form.current_price.data
            previous_price = form.previous_price.data
            in_stock = form.in_stock.data
            flash_sale = form.flash_sale.data

            file = form.product_picture.data
            file_name = secure_filename(file.filename)# removes whitespace and invalid characters from filename
            print('File name: ', file_name)
            file_path = os.path.join('website/static/images/' + file_name)
            print('File path: ', file_path)
            file.save(file_path)

            
            try:
                Product.query.filter_by(id=item_id).update(dict(product_name=product_name,
                                                                current_price=current_price, 
                                                                previous_price=previous_price,
                                                                in_stock=in_stock,
                                                                flash_sale=flash_sale,
                                                                product_picture=file_path))
                db.session.commit()
                flash(f'{product_name} updated Successfully')
                return redirect (url_for('admin.shop_items'))                          
            except Exception as e:
                print('Product not updated', e)
                flash('Item Not Updated')
        return render_template('update_item.html', form=form)


@admin.route('/update-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def update_item(item_id):
    if current_user.id == 1:
        item = Product.query.get_or_404(item_id)
        return redirect (url_for('admin.item_update', item_id=item.id))
    return render_template('404.html')



@admin.route('/delete-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def delete_item(item_id):
    if current_user.id == 1:
        try:
            item_to_delete = Product.query.get(item_id)
            db.session.delete(item_to_delete)
            db.session.commit()
            flash('One Item deleted')
            return redirect (url_for('admin.shop_items'))
        except Exception as e:
            print('Item not deleted', e)
            flash('Item not deleted')
        return redirect(url_for('admin.shop_items'))
    return render_template('404.html')


@admin.route('/view-orders')
@login_required
def order_view():
    if current_user.id == 1:
        orders = Order.query.all()
        for order in orders:
            if order.product_link:
                product_image_path=order.product.product_picture
                product_image_path = product_image_path.split('/')[2:]
                final_product_image_path = '/'.join(product_image_path)
                print("order", final_product_image_path)
                #print("order ", product_image_path)
        return render_template('view_orders.html', orders=orders)
    return render_template('404.html')

@admin.route('/update-order/<int:order_id>',methods=['GET', 'POST'])
@login_required
def update_order(order_id):
    if current_user.id ==1:
        form = OrderForm()

        return render_template('order_update.html', form=form)
    
    return render_template('404.html')