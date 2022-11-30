from rangefilter.filter import DateRangeFilter
from django.contrib import admin
from mobile.models import Call


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    list_display = ('id', 'user', 'call_duration', 'amount',)
    list_display_links = ('id',)
    fields = ('user', 'call_duration', 'amount', 'created_at',)
    readonly_fields = ('user', 'call_duration', 'amount', 'created_at',)

    list_filter = (
        ('created_at', DateRangeFilter),
    )
