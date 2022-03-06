import factory
from faker import Factory
from tradecore_api.models import User

faker = Factory.create()

class UserFactory(factory.django.DjangoModelFactory):
    """
    This a class for creating user objects
    """
    class Meta:
        model = User

    first_name = faker.first_name()
    last_name = faker.last_name()
    password = faker.password()
    email = faker.email()
    geolocation_data = {"null": "null"}
