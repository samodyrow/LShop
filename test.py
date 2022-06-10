from distutils.command.config import config
from itertools import product
import unittest
from config import Config
from app import db, create_app
from app.models import Product, User

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class UserTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user(self):
        user = User(username='alex')
        user.set_pswd('dfdfsdf')
        db.session.add(user)
        db.session.commit()
        user = User.query.first()
        self.assertEqual(user.username, 'alex' )
        self.assertNotEqual(user.username, 'alexandr')
        self.assertTrue(user.check_pswd('dfdfsdf'))
        self.assertFalse(user.check_pswd('dfdfsf'))
    
    def test_product(self):
        user = User(username='alex')
        user.set_pswd('1111')
        db.session.add(user)
        db.session.commit()

        user2 = User(username='alex1')
        user2.set_pswd('1111')
        db.session.add(user2)
        db.session.commit()
        
        product = Product(name='Product1', description='descr1', price=1, author=user)
        db.session.add(product)
        db.session.commit()
        product = Product.query.first()

        product2 = Product(name='Product2', description='descr2', price=100, author=user2)
        db.session.add(product2)
        db.session.commit()
        product = Product.query.first()

        self.assertEqual(product.name, 'Product1')
        self.assertNotEqual(product.name, 'Product2')
        self.assertEqual(product.author, user)
        self.assertNotEqual(product.author, user2)

        self.assertNotEqual(product2.name, 'Product1')
        self.assertEqual(product2.name, 'Product2')
        self.assertEqual(product2.author, user2)
        self.assertNotEqual(product2.author, user)

if __name__ == '__main__':
    unittest.main()