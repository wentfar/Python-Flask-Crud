from flask import Flask
from app.configs import Config
from app.models import db
from app.routes import tempBp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.app = app
    db.init_app(app)

    app.register_blueprint(tempBp)

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    return app
