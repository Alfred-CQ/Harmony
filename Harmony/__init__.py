from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()

base_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = base_dir + "/db"


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        db_dir, "harmony.sqlite"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import bp as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
