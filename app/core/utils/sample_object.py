from django.contrib.auth import get_user_model

from core.models import Tag, Ingredient, Recipe


def sample_user(email='admin@gmail.com', password='testpassword'):
    """Creates and return a sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_superuser(email='admin@gmail.com', password='testpassword'):
    """Creates and return a sample super user"""
    return get_user_model().objects.create_superuser(email, password)


def sample_tag(user, name='Test Tag'):
    """Create and return a sample tag"""
    return Tag.objects.create(user=user, name=name)


def sample_ingredient(user, name='Test Ingredient'):
    """Create and return a sample Ingredient"""
    return Ingredient.objects.create(user=user, name=name)


def sample_recipe(user, **params):
    """Create and return a sample recipe"""
    defaults = {
        'title': 'sample recipe',
        'time_minutes': 10,
        'price': 5.00
    }
    defaults.update(params)

    return Recipe.objects.create(user=user, **defaults)
