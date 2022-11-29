import pytest
import math
import random
from mobile.constants import MILLISECOND_PER_BLOCK
from tests.factories.call_factory import CallFactory
from tests.factories.user_factory import UserFactory
from tests.conftest import api_client

pytestmark = pytest.mark.django_db


@pytest.fixture
def have_data():
    user = UserFactory()
    call_count = 10
    block_count = 0
    for _ in range(call_count):
        call_duration = random.randint(1, 50) * 1000
        amount = math.ceil(call_duration/MILLISECOND_PER_BLOCK)
        CallFactory(user=user, call_duration=call_duration, amount=amount)
        block_count += amount
    return {
        'user': user,
        'call_count': call_count,
        'block_count': block_count
    }


def test_success__get_billing__have_data(have_data, api_client):
    user = have_data['user']
    call_count = have_data['call_count']
    block_count = have_data['block_count']
    response = api_client.get(
        path=f'/api/v1/mobile/{user.username}/billing/'
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['call_count'] == call_count
    assert response_data['block_count'] == block_count


@pytest.fixture
def have_no_data():
    user = UserFactory()
    call_count = 0
    block_count = 0
    return {
        'user': user,
        'call_count': call_count,
        'block_count': block_count
    }


def test_success__get_billing__have_no_data(have_no_data, api_client):
    user = have_no_data['user']
    call_count = have_no_data['call_count']
    block_count = have_no_data['block_count']
    response = api_client.get(
        path=f'/api/v1/mobile/{user.username}/billing/'
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data['call_count'] == call_count
    assert response_data['block_count'] == block_count


def test_fail__get_billing__username_invalid(api_client):
    username = 'username_invalid'
    response = api_client.get(
        path=f'/api/v1/mobile/{username}/billing/'
    )

    assert response.status_code == 400
    response_data = response.json()
    assert response_data['user'][0] == 'username is invalid.'