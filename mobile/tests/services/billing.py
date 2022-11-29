import pytest
import math
import random
from mobile.constants import MILLISECOND_PER_BLOCK
from tests.factories.call_factory import CallFactory
from tests.factories.user_factory import UserFactory
from mobile.services import BillingService

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


def test_success__export_billing__have_data(have_data):
    call_count = have_data['call_count']
    block_count = have_data['block_count']
    service = BillingService(have_data['user'])
    result = service.export_billing()
    assert result['call_count'] == call_count
    assert result['block_count'] == block_count


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


def test_success__export_billing__have_no_data(have_no_data):
    call_count = have_no_data['call_count']
    block_count = have_no_data['block_count']
    service = BillingService(have_no_data['user'])
    result = service.export_billing()
    assert result['call_count'] == call_count
    assert result['block_count'] == block_count
