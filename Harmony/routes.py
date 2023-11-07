from flask import render_template, jsonify, request, Blueprint, redirect, url_for
import os
import json

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["search"]
        if query != "":
            return redirect(url_for("main.search_results", query=query))
    return render_template("index.html")


@bp.route("/search_results/<query>")
def search_results(query):
    return render_template("search_results.html", query=query)
