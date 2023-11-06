from flask import Flask
from flask_pymongo import PyMongo
from flask_apscheduler import APScheduler
from .utils import (
    load_and_move_data,
)

mongo = PyMongo()
scheduler = APScheduler()

UPLOAD_FOLDER = "/home/alfred_suz/Documents/Proyectos/Harmony/app/data"
ALLOWED_EXTENSIONS = {"json"}


def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/harmony_db"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["ALLOWED_EXTENSIONS"] = ALLOWED_EXTENSIONS

    mongo.init_app(app)

    def schedule_data_load():
        with app.app_context():
            load_and_move_data(app)

    scheduler.init_app(app)
    scheduler.start()

    scheduler.add_job(
        id="Scheduled Data Load",
        func=schedule_data_load,
        trigger="cron",
        hour=7,
        minute=43,
    )

    from .routes import bp as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
