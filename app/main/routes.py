from app.models import User, Product
from flask import render_template
from app.main import bp
from flask_login import login_required


@bp.route('/')
@login_required
def index():
    products = Product.query.all()
    return render_template('main/index.html', title='Главная', products=products)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    return render_template('main/user.html', title='Пользователь', user=user)