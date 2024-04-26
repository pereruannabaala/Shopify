from flask import flask



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hbnwdvbn ajnbsjn ahe'

    return app

