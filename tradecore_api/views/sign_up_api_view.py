from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from tradecore_api.serializers import UserSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework import status
import os

from tradecore_api.utils.account_utility import AccountUtility

load_dotenv()


class SignUpAPIView(APIView):
    """
    This class handles signup api endpoint
    """

    permission_class = (AllowAny,)

    def post(self, request):
        """
        Handle POST request, create user in the database and return success/failure messages
        along with HTTP status code
        """
        ip = request.META.get("REMOTE_ADDR", '')
        geolocation_data = AccountUtility.get_geolocation_data(ip)
        request.data["geolocation_data"] = geolocation_data
        request.data["joined_on_holiday"] =AccountUtility.get_holiday_data(geolocation_data)
        user = request.data
        try:
            serializer = UserSerializer(data=user)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)
            validate_password(request.data["password"])
            serializer.save()
        except ValidationError as err:
            return Response(
                {"validation error": err}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.data, status=status.HTTP_200_OK)
