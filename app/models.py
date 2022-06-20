from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True)
    hash_pswd = db.Column(db.String(128))
    products = db.relationship('Product', backref='author', lazy=True)

    def set_pswd(self, password):
        self.hash_pswd = generate_password_hash(password)

    def check_pswd(self, password):
        return check_password_hash(self.hash_pswd, password)

    def __repr__(self) -> str:
        return '<User name - {}>'.format(self.username)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    description = db.Column(db.String(140))
    price = db.Column(db.Float)
    photo_path = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   

    def __repr__(self) -> str:
        return "<Product {}>".format(self.name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))