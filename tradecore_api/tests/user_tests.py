from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tradecore_api.tests.factories import UserFactory
from tradecore_api.models import User
from faker import Factory

faker = Factory.create()


class UserTests(APITestCase):
    """
    This is a class for testing login endpoints
    """

    def test_login_with_valid_creds(self):
        """
        Test login with valid credentials
        """
        user = UserFactory.create()
        user.save()
        response = self.client.post(reverse("login"), data={"email": user.email, "password": user.password}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_with_invalid_creds(self):
        """
        Test login with invalid credentials
        """
        user = UserFactory.create()
        user.save()
        response = self.client.post(reverse("login"), data={"email": user.email, "password": "invalid"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_with_invalid_params(self):
        """
        Test login with invalid params
        """
        response = self.client.post(reverse("login"), data={"user": "abc", "password": "123"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_creation(self):
        """
        Test to check user creation with valid data
        """
        user = UserFactory.create()
        self.assertEqual(User.objects.last().id, user.id)

    def test_user_signup_with_valid_params(self):
        """
        Test to check user signup with valid params
        """
        data = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email(),
            "password": faker.password()
        }

        response = self.client.post(reverse("signup"), data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_signup_with_invalid_params(self):
        """
        Test to check user signup with invalid params
        """
        data = {
            "first_name": 123,
            "last_name": faker.last_name(),
            "email": faker.email(),
            "password": faker.password()
        }

        response = self.client.post(reverse("signup"), data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
