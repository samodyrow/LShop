from flask import flash, redirect, render_template, url_for
from flask_login import current_user
from app import db
from app.product import bp
from app.product.forms import ProductForm
from app.models import Product
from config import Config

@bp.route('/new_product', methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        flash('Продукт добавлен') 
        product = Product(name=form.name.data, description=form.description.data, price=form.price.data, author=current_user)
        if form.photo.data.filename:
            product.photo_path = Config().IMG_PATH + form.photo.data.filename
            form.photo.data.save(Config().IMG_PATH + form.photo.data.filename)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for('main.index'))
    else:
        return render_template('product/new_product.html', title='Добавть товар', form=form)