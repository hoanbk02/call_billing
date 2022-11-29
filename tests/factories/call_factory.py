import factory
from factory.django import DjangoModelFactory
from tests.factories.user_factory import UserFactory
from mobile.models import Call


class CallFactory(DjangoModelFactory):
    class Meta:
        model = Call

    user = factory.SubFactory(UserFactory)
