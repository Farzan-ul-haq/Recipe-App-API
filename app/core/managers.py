from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new User"""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        print(user.email)
        return user
