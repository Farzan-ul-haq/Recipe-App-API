from django.test import TestCase

from app.calc import add, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)
        
    def test_subract_numbers(self):
        """Test that two numbers are subracted together"""
        self.assertEqual(sub(10, 5), 5)
