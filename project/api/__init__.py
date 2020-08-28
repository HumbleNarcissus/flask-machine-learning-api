import os

from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pickle

db = SQLAlchemy()
migrate = Migrate()

def create_app(script_info=None):
    """
    Creating and configurating app
    """
    app = Flask(__name__)

    # config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    api = Api(app)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # init api resources routes
    from api.resources.comment_prediction import PredictSentiment
    api.add_resource(PredictSentiment, '/prediction/<comment>')

    # init static routes with static resources
    @app.route("/")
    def index():
        return render_template("index.html")

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app