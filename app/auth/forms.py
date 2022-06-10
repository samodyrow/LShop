from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from app.models import User


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(message='Введите имя')])
    pswd = PasswordField('Пароль', validators=[
                                    Length(min=3, max=50, message='Пароль должен содержать от 3 до 50 символов'), 
                                    EqualTo('confirm_pwsd',message='Пароли не совпадают')
                                    ])
    confirm_pwsd = PasswordField('Повторите пароль')
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Имя пользователя {} уже занято'.format(username.data))


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(message='Введите имя')])
    pswd = PasswordField('Пароль', validators=[
                Length(min=3, max=50, message='Пароль должен содержать от 3 до 50 символов')])
    submit = SubmitField('Войти')
