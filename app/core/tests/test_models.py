from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='admin@gmail.com', password='testpassword'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def setUp(self):
        self.email = 'farzanulhaq123@gmail.com'
        self.superuser_email = 'admin@gmail.com'
        self.password = 'testpassword'
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

    def test_new_user_invalid_email(self):
        """Test creating user with email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password=self.password
            )

    def test_create_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email=self.superuser_email,
            password=self.password,
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
