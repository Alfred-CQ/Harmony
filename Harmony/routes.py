from flask import render_template, jsonify, current_app, Blueprint, redirect, url_for
import os
import json

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")
