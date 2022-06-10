from app import db
from app.auth import bp
from flask import flash, render_template, url_for, redirect
from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from flask_login import login_user, login_user, current_user, logout_user


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('{} - вы уже авторизованы'.format(current_user.username))
        redirect(url_for('main.index')) 
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_pswd(form.pswd.data):
            flash('{} рады что вы вернулись'.format(user.username))
            login_user(user)
            return redirect(url_for('main.index')) 
        else:
            flash('Неправильный логин или пароль')
            return redirect(url_for('auth.login'))   
    else:
        return render_template('auth/login.html', title='Авторизация', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_pswd(form.pswd.data)
        db.session.add(user)
        db.session.commit()
        flash('{} - вы успешно зарегистрировались'.format(form.username.data))
        return redirect(url_for('main.index'))
    else:
        return render_template('auth/register.html', title='Регистрация', form=form)

@bp.route('/logout')
def logout():
    flash('Вы вышли из личного кабинета')
    logout_user()
    return redirect(url_for('main.index'))