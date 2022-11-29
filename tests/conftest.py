import pytest
from django.test import Client
from rest_framework.test import APIClient


@pytest.fixture(scope='module')
def django_client():
    return Client()


@pytest.fixture(scope='module')
def api_client():
    return APIClient()
