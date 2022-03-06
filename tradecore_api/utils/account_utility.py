import datetime
import json
import os

import jwt
import requests
from rest_framework_jwt.utils import jwt_payload_handler
from tradecore_api.models import User, Post

DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0",
    "Accept-Encoding": "br, gzip, deflate",
    "Accept": "*/*",
    "Connection": "keep-alive",
}
MAX_RETRIES = 3

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
session.mount("https://", adapter)
session.mount("http://", adapter)


class AccountUtility:
    """
    This is a class for providing user accounts related functionality
    """

    @classmethod
    def validate_account_params(cls, email, password):
        """
        Method to validate params for login
        """
        valid = True
        if not email or not password:
            valid = False
        if type(email) is not str or type(password) is not str:
            valid = False
        return valid

    @classmethod
    def validate_post_params(cls, id, action):
        """
        Method to validate params for post
        """
        valid = True
        if not id or type(id) is not str:
            valid = False
        if not action or type(action) is not str or action not in ["like", "unlike"]:
            valid = False
        return valid

    @classmethod
    def get_geolocation_data(cls, ip):
        """
        Method to get geolocation_data of client from IP
        """
        url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={os.environ.get('ABSTRACT_GEOLOCATION_API_KEY')}&ip_address={ip}"
        response = session.get(url, headers=DEFAULT_REQUEST_HEADERS, timeout=10)
        geolocation_data = (
            json.loads(response.content) if response.status_code == 200 else {}
        )
        return geolocation_data

    @classmethod
    def get_holiday_data(cls, geolocation_data):
        country = geolocation_data.get("country_code")
        year, month, day = (
            datetime.date.today().year,
            datetime.date.today().month,
            datetime.date.today().day,
        )
        url = f"https://holidays.abstractapi.com/v1/?api_key={os.environ.get('ABSTRACT_HOLIDAYS_API_KEY')}&country={country}&year={year}&month={month}&day={day}"
        if country:
            response = session.get(url, headers=DEFAULT_REQUEST_HEADERS, timeout=10)
            holiday_flag = (
                True
                if json.loads(response.content) and response.status_code == 200
                else False
            )
        else:
            holiday_flag = False
        return holiday_flag

    @classmethod
    def get_token(cls, user):
        """
        Takes in a user object, returns a authentication token.
        """
        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, os.environ.get("SECRET_KEY"))
        return token

    @classmethod
    def get_user_data(cls, jwt_token):
        """
        Takes in jwt token, returns user data
        """
        try:
            user_data = jwt.decode(jwt_token[4:], os.environ.get("SECRET_KEY"))
            user = User.objects.get(email=user_data["email"])
            return user
        except Exception as exc:
            return None

    @classmethod
    def check_post_authorization(cls, user, post_id):
        """
        Takes in a user object, checks authorization for post
        """
        try:
            post = Post.objects.get(id=post_id)
            return True if post.user == user else False
        except Exception as exc:
            return False
