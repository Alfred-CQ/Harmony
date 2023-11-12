from flask import render_template, request, redirect, url_for

from app.routes import bp
from app.models.document import Document
from app.models.word import Word


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["search"]
        if query != "":
            return redirect(url_for("main.search_results", query=query))
    return render_template("index.html")


@bp.route("/search_results/<query>")
def search_results(query):
    documents = (
        Document.query.join(Word, Document.doc_id == Word.doc_id)
        .filter(Word.word == query)
        .all()
    )

    return render_template("search_results.html", query=query, documents=documents)
