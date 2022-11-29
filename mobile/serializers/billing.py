from rest_framework import serializers


class GetBillingSerializerV1(serializers.Serializer):
    call_count = serializers.IntegerField()
    block_count = serializers.IntegerField()
