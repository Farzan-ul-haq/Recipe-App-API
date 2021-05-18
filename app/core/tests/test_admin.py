from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.email = 'farzanulhaq123@gmail.com'
        self.name = 'Farzan'
        self.superuser_name = 'Admin'
        self.superuser_email = 'admin@gmail.com'
        self.password = 'testingpassword'
        self.client = Client()

        self.user = get_user_model().objects.create_superuser(
            email=self.email,
            password=self.password,
            name=self.name
        )
        self.super_user = get_user_model().objects.create_superuser(
            email=self.superuser_email,
            password=self.password
        )
        self.client.force_login(self.super_user)

    def test_user_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        resp = self.client.get(url)

        self.assertContains(resp, self.user.name)
        self.assertContains(resp, self.user.name)

    def test_user_change_page(self):
        """TEst that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_create_user_page(self):
        """Test taht the create user page works"""
        url = reverse('admin:core_user_add')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
