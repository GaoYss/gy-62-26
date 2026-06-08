from django.contrib import admin

from .models import EmergencyNotification


@admin.register(EmergencyNotification)
class EmergencyNotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "target_group", "is_active", "published_at")
    search_fields = ("title", "content")
    list_filter = ("level", "target_group", "is_active")
