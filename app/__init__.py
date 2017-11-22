"""Imports the necessary modules and sets up the app"""
from flask import Flask
from config import config

def create_app(configuration):
    """Initializes the app"""
    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)

    return app
