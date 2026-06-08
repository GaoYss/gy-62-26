from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("resident", "family_name", "family_phone", "visit_time", "visitor_count", "status")
    search_fields = ("resident__name", "family_name", "family_phone")
    list_filter = ("status", "visit_time")
