from rest_framework.views import APIView
from tradecore_api.models import Post
from tradecore_api.serializers import PostSerializer
from tradecore_api.utils import AccountUtility
from tradecore_api.models import User
from rest_framework.response import Response
from rest_framework import status


class PostAPIView(APIView):
    """
    This class handles post endpoint
    """

    def post(self, request):
        """
        Handle POST request, check authenticated user, creates post and returns response along with HTTP status code
        """
        pass
