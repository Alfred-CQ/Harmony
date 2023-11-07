from flask import render_template, jsonify, request, Blueprint, redirect, url_for
import os
import json

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["search"]
        return redirect(url_for("search_results", query=query))
    return render_template("index.html")
