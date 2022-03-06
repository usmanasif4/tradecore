from rest_framework.views import APIView
from tradecore_api import serializers
from tradecore_api.models import Post
from tradecore_api.serializers import PostSerializer
from tradecore_api.utils import AccountUtility
from tradecore_api.models import User
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError


class PostAPIView(APIView):
    """
    This class handles post endpoint
    """

    def post(self, request):
        """
        Handle POST request, checks authenticated user, creates post and returns response along with HTTP status code
        """
        user = AccountUtility.get_user_data(request.headers.get("Authorization", None))
        if user:
            try:
                serializer = PostSerializer(data=request.data)
                if not serializer.is_valid():
                    raise ValidationError(serializer.errors)
                serializer.save(user=user)
                return Response(
                    {"post_data": serializer.data}, status=status.HTTP_200_OK
                )
            except ValidationError as err:
                return Response(
                    {"validation error": err}, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"message": "User is not authenticated"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    def get(self, request):
        """
        Handles GET request, checks authenticated user, returns post of the user
        """
        user = AccountUtility.get_user_data(request.headers.get("Authorization", None))
        if user:
            post_data = Post.objects.filter(user=user)
            serializer = PostSerializer(post_data, many=True)
            return Response({"posts": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "User is not authenticated"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    def patch(self, request):
        """
        Handle PATCH request, checks authenticated user, likes/unlikes a post based on action
        """
        user = AccountUtility.get_user_data(request.headers.get("Authorization", None))
        if user:
            post_id = request.data.get("post_id", None)
            action = request.data.get("action", None)
            if AccountUtility.validate_post_params(post_id, action):
                try:
                    post = Post.objects.get(id=post_id)
                    if action == "like":
                        post.like.add(user)
                    elif action == "unlike" and user in post.like.all():
                        post.like.remove(user)
                    post.save()
                    return Response(
                        {"message": "Action performed successfully"},
                        status=status.HTTP_200_OK,
                    )
                except Exception as exc:
                    return Response(
                        {"msg": "Unable to like/unlike post"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
            else:
                return Response(
                    {
                        "message": "Please provide post_id (str) and action (str)(like,unlike) in params"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"message": "User is not authenticated"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
