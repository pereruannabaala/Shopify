from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# SQLAlchemy instance
db = SQLAlchemy()
DB_NAME = 'database.sqlite3'

def create_database(app):
    """
    Create the database tables based on the defined models.
    """
    with app.app_context():
        db.create_all()
    print('Database created')

def create_app():
    """
    Create the Flask application instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hbnwdvbn ajnbsjn ahe'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///' + DB_NAME

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    login_manager =LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
        return Customer.query.get(int(id))

    # Importing blueprints
    from .views import views
    from .auth import auth
    from .admin import admin
    from .models import Customer, Product, Cart, Order

    # Registering blueprints
    app.register_blueprint(views, url_prefix='/')  # localhost:5000/about-us
    app.register_blueprint(auth, url_prefix='/auth')  # localhost:5000/auth/change-password
    app.register_blueprint(admin, url_prefix='/admin')

    # Creating database
    create_database(app)

    return app

