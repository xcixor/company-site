"""Defines the route for the homepage"""

from flask import render_template, url_for

from app.landing import landing

@landing.route('/')
def index():
    """Presents the home page"""
    return render_template('index.html')

def sample_test(status):
    """Just a method"""
    if status == 400:
        return True