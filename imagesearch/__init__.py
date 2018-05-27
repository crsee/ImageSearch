"""
Exports a function to create an instance of ImageSearch app.
"""

import os

from flask import Flask, render_template
from flask_mongoengine import MongoEngine

def create_app():    
    app = Flask(__name__, instance_relative_config=True)

    # load default config
    app.config.from_object("config.Default")

    # load instance config (if present)
    app.config.from_pyfile("config.py", silent=True)

    # load environment variables (if present)
    app.config.update({
        "DEBUG": os.environ.get("DEBUG", str(app.config.get("DEBUG"))).lower() == "true",
        "SECRET_KEY": os.environ.get("SECRET_KEY", app.config.get("SECRET_KEY")),
        "SERVER_NAME": os.environ.get("SERVER_NAME", app.config.get("SERVER_NAME")),
        "MONGODB_DB": os.environ.get("MONGODB_DB", app.config.get("MONGODB_DB")),
        "MONGODB_HOST": os.environ.get("MONGODB_HOST", app.config.get("MONGODB_HOST")),
        "MONGODB_PORT": os.environ.get("MONGODB_PORT", app.config.get("MONGODB_PORT")),
        "MONGODB_USERNAME": os.environ.get("MONGODB_USERNAME", app.config.get("MONGODB_USERNAME")),
        "MONGODB_PASSWORD": os.environ.get("MONGODB_PASSWORD", app.config.get("MONGODB_PASSWORD")),
        "GOOGLE_API_KEY": os.environ.get("GOOGLE_API_KEY", app.config.get("GOOGLE_API_KEY")),
        "GOOGLE_CSE_ID": os.environ.get("GOOGLE_CSE_ID", app.config.get("GOOGLE_CSE_ID"))
    })

    # connect to database
    MongoEngine(app)

    # disable strict trailing slashes
    app.url_map.strict_slashes = False

    # register blueprints
    from .blueprints import home
    app.register_blueprint(home)

    # attach 404 error handler
    @app.errorhandler(404)
    def handle_404(error):
        return render_template("404.html", error=error), 404

    return app