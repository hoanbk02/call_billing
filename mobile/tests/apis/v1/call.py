import json
import pytest
import math
import random
from mobile.constants import MILLISECOND_PER_BLOCK
from tests.factories.user_factory import UserFactory
from mobile.models import Call
from tests.conftest import api_client

pytestmark = pytest.mark.django_db


def test_success__create_call(api_client):
    user = UserFactory()

    call_duration = random.randint(1, 5*60) * 1000
    response = api_client.put(
        path=f'/api/v1/mobile/{user.username}/call/',
        data=json.dumps({
            'call_duration': call_duration
        }),
        content_type="application/json"
    )

    assert response.status_code == 201
    call_last = Call.objects.filter(user=user).last()
    assert call_last is not None
    assert call_last.call_duration == call_duration
    assert call_last.amount == math.ceil(call_duration / MILLISECOND_PER_BLOCK)


def test_fail__create_call__duration_is_negative(api_client):
    user = UserFactory()

    call_duration = random.randint(1, 5*60) * 1000
    response = api_client.put(
        path=f'/api/v1/mobile/{user.username}/call/',
        data=json.dumps({
            'call_duration': -call_duration
        }),
        content_type="application/json"
    )

    assert response.status_code == 400
    response_data = response.json()
    assert response_data['call_duration'][0] == "Ensure this value is greater than or equal to 1."


def test_fail__create_call__duration_is_zero(api_client):
    user = UserFactory()
    response = api_client.put(
        path=f'/api/v1/mobile/{user.username}/call/',
        data=json.dumps({
            'call_duration': 0
        }),
        content_type="application/json"
    )

    assert response.status_code == 400
    response_data = response.json()
    assert response_data['call_duration'][0] == "Ensure this value is greater than or equal to 1."


def test_fail__create_call__username_is_invalid(api_client):
    username = 'username_invalid'
    call_duration = random.randint(1, 5*60) * 1000
    response = api_client.put(
        path=f'/api/v1/mobile/{username}/call/',
        data=json.dumps({
            'call_duration': call_duration
        }),
        content_type="application/json"
    )

    assert response.status_code == 400
    response_data = response.json()
    assert response_data['user'][0] == "username is invalid."


def test_fail__create_call__username_and_duration_is_invalid(api_client):
    username = 'username_invalid'
    call_duration = random.randint(0, 5*60) * 1000
    response = api_client.put(
        path=f'/api/v1/mobile/{username}/call/',
        data=json.dumps({
            'call_duration': -call_duration
        }),
        content_type="application/json"
    )

    assert response.status_code == 400
    response_data = response.json()
    assert response_data['user'][0] == "username is invalid."
    assert response_data['call_duration'][0] == "Ensure this value is greater than or equal to 1."
