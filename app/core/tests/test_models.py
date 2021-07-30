from django.test import TestCase

from core.utils.sample_object import sample_user, sample_superuser, \
                                     sample_tag, sample_ingredient, \
                                     sample_recipe


class ModelTests(TestCase):

    def setUp(self):
        self.email = 'farzanulhaq123@gmail.com'
        self.superuser_email = 'admin@gmail.com'
        self.password = 'testpassword'
        self.destabilize_email = 'farzan@GMAIL.COM'
        self.normalize_email = self.destabilize_email.lower()

    def test_create_user_with_email_successful(self):
        """Test creating a new user with a email is successful"""
        user = sample_user(email=self.email, password=self.password)

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        user = sample_user(email=self.destabilize_email,
                           password=self.password)

        self.assertEqual(user.email, self.normalize_email)

    def test_new_user_invalid_email(self):
        """Test creating user with email raises error"""
        with self.assertRaises(ValueError):
            sample_user(email=None, password=self.password)

    def test_create_super_user(self):
        """Test creating a new superuser"""
        user = sample_superuser(email=self.superuser_email,
                                password=self.password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = sample_tag(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test that ingredient string representation"""
        ingredient = sample_ingredient(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test that ingredient string representation"""
        recipe = sample_recipe(
            user=sample_user(),
            title="Steak and ushroom Sauce",
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)
