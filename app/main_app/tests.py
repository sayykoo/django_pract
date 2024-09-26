from django.test import TestCase
from django.urls import reverse
from .models import RegisterForm
from django.contrib.auth.models import User


class TestCaseViewAccount(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'username': 'ASD',
            'email': 'asd@gmail.com',
            'password1': 'asd123iQ3344',
            'password2': 'asd123iQ3344',
        }
        
    def test_register_view(self):
        RegisterForm(data = self.form_data)
        self.client.post(reverse('register'), data = self.form_data)
        user = User.objects.filter(username = self.form_data['username']).exists()
        self.assertTrue(user)