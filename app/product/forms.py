from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired,Length


class ProductForm(FlaskForm):
    name = StringField("Название", validators=[Length(min=3, max=50, message='Название должно содержать от 3 до 50 символов')])
    description = TextAreaField("Описание", validators=[DataRequired(), Length(min=0, max = 140, message='Описание больше 140 символов')] )
    price = FloatField("Цена, рублей", validators=[DataRequired(message='Укажите цену в рублях')])
    photo = FileField("Фото товара")
    submit = SubmitField("Добавить")