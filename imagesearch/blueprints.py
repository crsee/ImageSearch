"""
Exports ImageSearch app blueprints.
"""

from flask import Blueprint, render_template

home = Blueprint("home", __name__, url_prefix="/")

@home.route("/")
def index():
    return render_template("home.html")