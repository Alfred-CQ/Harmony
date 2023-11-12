from flask import Flask

from config import Config

from app.extensions.sqlite import db
from app.models.document import Document
from app.models.word import Word


def create_app(config_class=Config):
    app = Flask(
        __name__,
        static_folder=Config.STATIC_FOLDER,
        template_folder=Config.TEMPLATE_FOLDER,
    )

    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import bp as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
