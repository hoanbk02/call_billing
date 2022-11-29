import math
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from call_billing.repository import UserRepository
from mobile.repositories import CallRepository
from mobile.constants import MILLISECOND_PER_BLOCK


class CreateCallSerializerV1(serializers.Serializer):
    user = serializers.CharField(min_length=5, max_length=32)
    call_duration = serializers.IntegerField(min_value=0)

    def validate_user(self, value):
        user = UserRepository.get_by_username(username=value)
        if not user:
            raise ValidationError({'username': 'username is invalid'})
        return user

    def create(self, validated_data):
        validated_data['amount'] = math.ceil(validated_data['call_duration']/MILLISECOND_PER_BLOCK)
        return CallRepository.create_object(**validated_data)
