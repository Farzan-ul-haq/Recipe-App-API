from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def setUp(self):
        self.email = 'farzanulhaq123@gmail.com'
        self.password = 'farzanulhaq'
        self.destabilize_email = 'farzan@GMAIL.COM'
        self.normalize_email = self.destabilize_email.lower()

    def test_create_user_with_email_successful(self):
        """Test creating a new user with a email is successful"""
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        user = get_user_model().objects.create_user(
            email=self.destabilize_email,
            password=self.password,
        )

        self.assertEqual(user.email, self.normalize_email)
