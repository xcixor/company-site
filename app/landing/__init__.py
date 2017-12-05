"""This is the constructor for the landing blueprint.
"""
from flask import Blueprint

landing = Blueprint('landing', __name__)

# from . import views

from app.landing import views
