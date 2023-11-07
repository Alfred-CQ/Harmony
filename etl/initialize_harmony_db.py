from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import json
import argparse

Base = declarative_base()


class Document(Base):
    __tablename__ = "documents"

    doc_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)


class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    doc_id = Column(Integer, ForeignKey("documents.doc_id"), nullable=False)


def init_db():
    engine = create_engine("sqlite:///../Harmony/db/harmony.sqlite")
    Base.metadata.create_all(engine)
    return engine


def load_documents(session_factory, json_file):
    with session_factory() as session:
        with session.begin():
            with open(json_file, "r") as file:
                for line in file:
                    try:
                        doc_data = json.loads(line)
                        document = Document(
                            doc_id=doc_data["id"],
                            title=doc_data["title"],
                            description=doc_data["description"],
                            url=doc_data["url"],
                        )
                        session.add(document)
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        continue


def load_words(session_factory, json_file):
    with session_factory() as session:
        with session.begin():
            with open(json_file, "r") as file:
                for line in file:
                    try:
                        word_data = json.loads(line)
                        word = word_data["word"]
                        document_ids = word_data["documents"]

                        for doc_id in document_ids:
                            exists = (
                                session.query(Document.doc_id)
                                .filter_by(doc_id=doc_id)
                                .scalar()
                                is not None
                            )
                            if exists:
                                association_entry = Word(word=word, doc_id=doc_id)
                                session.add(association_entry)
                            else:
                                print(
                                    f"Error: Document ID {doc_id} does not exist for word '{word}'"
                                )

                    except Exception as e:
                        print(f"An error occurred: {e}")
                        continue


def main(documents_ndjson, words_ndjson):
    engine = init_db()
    Session = sessionmaker(bind=engine)
    load_documents(Session, documents_ndjson)
    load_words(Session, words_ndjson)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load documents and words into Harmony database."
    )

    parser.add_argument(
        "documents_json_path", type=str, help="Path to the documents ndjson file"
    )

    parser.add_argument(
        "words_json_path", type=str, help="Path to the words ndjson file"
    )

    args = parser.parse_args()

    main(args.documents_json_path, args.words_json_path)
