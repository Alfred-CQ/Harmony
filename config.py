import os

base_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = base_dir + "/app" + "/db"


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI"
    ) or "sqlite:///" + os.path.join(db_dir, "harmony.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"
