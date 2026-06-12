from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_datetime

from backend.residents.models import Resident
from backend.residents.services import serialize_resident

from .models import Appointment


WRITE_FIELDS = [
    "resident",
    "resident_id",
    "family_name",
    "family_phone",
    "relationship",
    "visit_time",
    "visitor_count",
    "status",
    "notes",
]

VALID_STATUSES_FOR_LIMIT = ["pending", "approved", "completed"]


def serialize_appointment(appointment):
    return {
        "id": appointment.id,
        "resident": serialize_resident(appointment.resident),
        "resident_id": appointment.resident_id,
        "family_name": appointment.family_name,
        "family_phone": appointment.family_phone,
        "relationship": appointment.relationship,
        "visit_time": appointment.visit_time.isoformat(),
        "visitor_count": appointment.visitor_count,
        "status": appointment.status,
        "notes": appointment.notes,
        "created_at": appointment.created_at.isoformat(),
        "updated_at": appointment.updated_at.isoformat(),
    }


def normalize_payload(payload):
    data = {field: payload.get(field) for field in WRITE_FIELDS if field in payload}
    if "resident" in data:
        data["resident_id"] = data.pop("resident")
    if "visit_time" in data and isinstance(data["visit_time"], str):
        data["visit_time"] = parse_datetime(data["visit_time"])
    return data


def list_appointments(status=None):
    queryset = Appointment.objects.select_related("resident")
    if status:
        queryset = queryset.filter(status=status)
    return [serialize_appointment(item) for item in queryset]


def get_week_range(dt):
    year, week, _ = dt.isocalendar()
    from datetime import date, timedelta
    jan4 = date(year, 1, 4)
    week_start = jan4 - timedelta(days=jan4.isoweekday() - 1) + timedelta(weeks=week - 1)
    week_end = week_start + timedelta(days=6)
    return week_start, week_end


def check_weekly_limit(resident_id, family_name, family_phone, visit_time, exclude_id=None):
    limit = getattr(settings, "APPOINTMENT_WEEKLY_LIMIT", 2)
    week_start, week_end = get_week_range(visit_time)
    queryset = Appointment.objects.filter(
        resident_id=resident_id,
        family_name=family_name,
        family_phone=family_phone,
        visit_time__date__gte=week_start,
        visit_time__date__lte=week_end,
        status__in=VALID_STATUSES_FOR_LIMIT,
    )
    if exclude_id:
        queryset = queryset.exclude(id=exclude_id)
    count = queryset.count()
    if count >= limit:
        raise ValidationError(
            f"同一家属对同一老人每周最多预约{limit}次，"
            f"本周已预约{count}次，请选择其他时间。"
        )


def create_appointment(payload):
    data = normalize_payload(payload)
    Resident.objects.get(pk=data["resident_id"])
    check_weekly_limit(
        resident_id=data["resident_id"],
        family_name=data["family_name"],
        family_phone=data["family_phone"],
        visit_time=data["visit_time"],
    )
    return Appointment(**data)


def update_appointment(appointment, payload):
    data = normalize_payload(payload)
    check_weekly_limit(
        resident_id=data.get("resident_id", appointment.resident_id),
        family_name=data.get("family_name", appointment.family_name),
        family_phone=data.get("family_phone", appointment.family_phone),
        visit_time=data.get("visit_time", appointment.visit_time),
        exclude_id=appointment.id,
    )
    for field, value in data.items():
        setattr(appointment, field, value)
    appointment.save()
    return appointment


def get_appointment_config():
    return {
        "weekly_limit": getattr(settings, "APPOINTMENT_WEEKLY_LIMIT", 2),
    }
