from call_billing.repository import BaseRepository
from mobile.models import Call


class CallRepository(BaseRepository):
    model = Call

    @classmethod
    def filter_by_user(cls, user):
        return cls.model.objects.filter(user=user)
