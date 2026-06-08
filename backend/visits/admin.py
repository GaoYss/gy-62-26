from django.contrib import admin

from .models import VisitRecord


@admin.register(VisitRecord)
class VisitRecordAdmin(admin.ModelAdmin):
    list_display = ("appointment", "check_in_time", "check_out_time", "visitor_temperature", "staff_name")
    search_fields = ("appointment__family_name", "appointment__resident__name", "staff_name")
