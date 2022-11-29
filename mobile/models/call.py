from django.db import models
from django.contrib.auth.models import User
from call_billing.models import TrackingAbstractModel


class Call(TrackingAbstractModel):
    user = models.ForeignKey(
        to=User, related_name="user_call",
        on_delete=models.PROTECT, blank=False, null=False
    )
    call_duration = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()