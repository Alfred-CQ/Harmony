from app.extensions.sqlite import db


class Document(db.Model):
    __tablename__ = "documents"

    doc_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    link = db.Column(db.String)
