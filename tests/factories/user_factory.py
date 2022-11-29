import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('email')
