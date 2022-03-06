from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tradecore_api.tests.factories import PostFactory
from tradecore_api.models import Post
from faker import Factory

faker = Factory.create()


class PostTests(APITestCase):
    """
    This is a class for testing login endpoints
    """
    def test_user_creation(self):
        """
        Test to check post creation with valid data
        """
        post = PostFactory.create()
        self.assertEqual(Post.objects.last().id, post.id)
