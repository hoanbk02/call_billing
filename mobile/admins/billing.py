from django.contrib import admin
from mobile.models import BillingManagement


@admin.register(BillingManagement)
class BillingManagementAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'call_count', 'block_count',)
    list_display_links = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
