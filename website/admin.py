from flask import Blueprint, render_template 
from flask_login import login_required, current_user
from .forms import ShopItemsForm

admin = Blueprint('admin',__name__)

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
            file_name = secure_filename(file.filename)


        return render_template('add-shop-items.html',form=form)
    return render_template('404.html')

