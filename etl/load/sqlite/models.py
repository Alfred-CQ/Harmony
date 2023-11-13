from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Document(Base):
    __tablename__ = "documents"
    doc_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    link = Column(String)


class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    doc_id = Column(Integer, ForeignKey("documents.doc_id"), nullable=False)
