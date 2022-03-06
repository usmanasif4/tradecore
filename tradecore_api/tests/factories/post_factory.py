import factory
from faker import Factory
from tradecore_api.models import Post

faker = Factory.create()

class PostFactory(factory.django.DjangoModelFactory):
    """
    This a class for creating post objects
    """
    class Meta:
        model = Post

    title = faker.text()
    description = faker.text()
    user = None
