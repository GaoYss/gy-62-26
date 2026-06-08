from django.contrib import admin

from .models import Resident


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "age", "room_number", "care_level", "emergency_contact")
    search_fields = ("name", "room_number", "emergency_contact")
    list_filter = ("care_level", "gender")
