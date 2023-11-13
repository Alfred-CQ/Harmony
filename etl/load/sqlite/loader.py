import json
import os

from .models import Document, Word
from .database import Session


def load_documents(documents_path):
    with Session() as session:
        for filename in os.listdir(documents_path):
            file_path = os.path.join(documents_path, filename)
            if os.path.isfile(file_path) and file_path.endswith(".json"):
                with open(file_path, "r") as file:
                    for line in file:
                        try:
                            doc_data = json.loads(line)
                            document = Document(
                                doc_id=doc_data["id"],
                                title=doc_data["title"],
                                description=doc_data["description"],
                                link=doc_data["link"],
                            )
                            session.add(document)
                        except Exception as e:
                            print(
                                f"An error occurred while processing file {filename}: {e}"
                            )
                            continue
        session.commit()


def load_words(json_file):
    with Session() as session:
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
                session.commit()
