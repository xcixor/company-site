"""Imports the necessary modules and sets up the app"""
from flask import Flask
from config import config

def create_app(configuration):
    """Initializes the app
    Args:
        configuration(class): Contains the configuration settings
    """
    #Create the app instance
    app = Flask(__name__)
    app.config.from_object(config[configuration])
    config[configuration].init_app(app)

    #Registering the landing blueprint
    #It is the root of the site so it does not require a url prefix, 
    #NB: it is important to import the blueprint after the app has been created otherwise it wont work
    from app.landing import landing as landing_blueprint
    app.register_blueprint(landing_blueprint)

    return app
