from rest_framework.views import APIView
from tradecore_api.models import Post
from tradecore_api.serializers import PostSerializer


class PostRetrieveUpdateDestroyAPIView(APIView):
    """
    This class handles post endpoints for specific post
    """

