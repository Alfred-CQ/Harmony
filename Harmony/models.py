from . import db


class Document(db.Model):
    __tablename__ = "documents"

    doc_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)


class Word(db.Model):
    __tablename__ = "words"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String, nullable=False)
    doc_id = db.Column(db.Integer, db.ForeignKey("documents.doc_id"), nullable=False)
