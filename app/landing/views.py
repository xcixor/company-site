"""Defines the route for the homepage"""

from flask import render_template, url_for

from app.landing import landing

@landing.route('/')
def index():
    """Presents the home page"""
    return render_template('index.html')