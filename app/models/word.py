from app.extensions.sqlite import db


class Word(db.Model):
    __tablename__ = "words"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String, nullable=False)
    doc_id = db.Column(db.Integer, db.ForeignKey("documents.doc_id"), nullable=False)
