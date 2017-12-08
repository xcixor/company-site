"""Tests the landing Blueprint"""

import unittest

from app import create_app

class TestLandingBlueprint(unittest.TestCase):
    """Tests the landing module"""

    def setUp(self):
        """Set up some stuff"""
        #create app with a test client
        self.app = create_app('testing').test_client()

    def tearDown(self):
        """Remove the stuff set up above"""
        pass

    def test_home_status_code(self):
        """Test whether home is being rendered appropriately"""
        # sends HTTP GET request to the application on the specified path
        response = self.app.get('/')
        # assert the response data
        self.assertEqual(response.status_code, 200)
        # useful tips on statuses at www.flaskapi.org
             

