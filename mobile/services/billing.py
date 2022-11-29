from django.db.models import Count, Sum
from mobile.repositories import CallRepository


class BillingService:
    def __init__(self, user):
        self.user = user

    def export_billing(self):
        query_billing = CallRepository.filter_by_user(
            self.user
        ).aggregate(Count('id'), Sum('amount'))
        return {
            'call_count': query_billing['id__count'],
            'block_count': query_billing['amount__sum'] or 0
        }
