from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from call_billing.repository import UserRepository


class UserSerializer(serializers.Serializer):
    user = serializers.CharField(min_length=5, max_length=32)

    def validate_user(self, value):
        user = UserRepository.get_by_username(username=value)
        if not user:
            raise ValidationError({'username': 'username is invalid'})
        return user
