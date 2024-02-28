from django.test import TestCase
from django.urls import reverse, reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

CREATE_USER_TOKEN_URL = reverse("authentication:auth-token")

class TripViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            email='testuser@mail.com',
            first_name='Test',
            last_name='Case',
            password='testpassword',
        )
        # Create a test user
        self.driver = get_user_model().objects.create_user(
            email='driveruser@mail.com',
            password='driverpassword',
            is_driver=True
        )
        # Create a test client
        self.client = APIClient()

        # Login the test user (assuming you have token authentication)
        # self.client.force_authenticate(user=self.user)

    def test_user_token(self):

        data= {
            "email": 'testuser@mail.com',
            "password": "testpassword",
        }
        # token
        token = Token.objects.get_or_create(user=self.user)
        response = self.client.post(CREATE_USER_TOKEN_URL, data, format='json')
        self.assertIn('token', response.data)
        self.assertEqual(token[0].key, response.data['token'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
