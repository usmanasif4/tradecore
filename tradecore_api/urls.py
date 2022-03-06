from django.contrib import admin
from django.urls import path
from tradecore_api.models.user import User

from tradecore_api.views.login_api_view import *
from tradecore_api.views.sign_up_api_view import SignUpAPIView
from tradecore_api.views.user_api_view import UserAPIView
from tradecore_api.views.login_api_view import LoginAPIView
from tradecore_api.views import PostAPIView
from tradecore_api.views import PostUpdateDestroyAPIView

urlpatterns = [
    path("login", LoginAPIView.as_view(), name="login"),
    path("signup", SignUpAPIView.as_view(), name="signup"),
    path("user/<int:id>", UserAPIView.as_view(), name="user"),
    path("post", PostAPIView.as_view(), name="post-get-create"),
    path(
        "post/<int:id>",
        PostUpdateDestroyAPIView.as_view(),
        name="post-update-delete",
    ),
]
