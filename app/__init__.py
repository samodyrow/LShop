from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap5()
login = LoginManager()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    login.init_app(app)
    login.login_view = 'auth.login'

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.product import bp as product_bp
    app.register_blueprint(product_bp)

    return app
