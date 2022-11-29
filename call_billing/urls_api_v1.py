from django.urls import path, include
from mobile.apis.v1 import CreateCallAPIView, GetBillingAPIView


urlpatterns = [
    path('mobile/<username>/', include([
        path('call/', CreateCallAPIView.as_view()),
        path('billing/', GetBillingAPIView.as_view())
    ])),
]
