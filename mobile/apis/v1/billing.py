from rest_framework.views import APIView
from rest_framework.response import Response
from call_billing.serializers import UserSerializer
from mobile.serializers import GetBillingSerializerV1
from mobile.services import BillingService


class GetBillingAPIView(APIView):

    def get(self, request, *args, **kwargs):
        request_data = {
            'user': self.kwargs['username']
        }
        serializer = UserSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        service = BillingService(serializer.validated_data['user'])
        data = service.export_billing()
        return Response(GetBillingSerializerV1(data).data)
