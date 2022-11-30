from django.db import models
from dbview.models import DbView
from mobile.models import Call


class BillingManagement(DbView):
    user_id = models.IntegerField(primary_key=True, db_column='user_id')
    username = models.CharField(max_length=32, db_column='username')
    call_count = models.IntegerField(db_column='call_count')
    block_count = models.IntegerField(db_column='block_count')

    @classmethod
    def view(cls):
        qs = Call.objects.values(
            'user__id',
            'user__username',
        ).annotate(
            call_count=models.Count('id'),
            block_count=models.Sum('amount'),
        ).order_by(
            'user__id'
        )
        return str(qs.query)
