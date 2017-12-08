"""Tests the landing Blueprint"""

import unittest

from app import landing

class TestLandingBlueprint(unittest.TestCase):
    """Tests the landing module"""

    def test_sampletest(self):
        """Sample test"""
        self.assertEqual(landing.views.sample_test(400), True)

    
