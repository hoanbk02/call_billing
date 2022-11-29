from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.serializers import CreateCallSerializerV1


class CreateCallAPIView(APIView):

    def put(self, request, *args, **kwargs):
        request_data = request.data
        request_data['user'] = self.kwargs['username']
        serializer = CreateCallSerializerV1(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
