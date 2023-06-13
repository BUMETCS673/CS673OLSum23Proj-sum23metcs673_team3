from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('User_Login')
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_valid_login(self):
        # Simulate a valid login request
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpass'})

        # Check if the user is redirected to the user page
        self.assertRedirects(response, reverse('user_page'))

    def test_invalid_login(self):
        response = self.client.post(self.login_url, {'username': 'invaliduser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertTrue(response.url.startswith('/login/user/'))

        # Follow the redirect
        redirect_response = self.client.get(response.url)
        self.assertEqual(redirect_response.status_code, 200)
        self.assertContains(redirect_response, '3', html=False)
        
    def test_get_login_page(self):
        # Simulate a GET request to the login page
        response = self.client.get(self.login_url)

        # Check if the response status is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used for rendering the login page
        self.assertTemplateUsed(response, 'login.html')