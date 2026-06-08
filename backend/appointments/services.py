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


def create_appointment(payload):
    data = normalize_payload(payload)
    Resident.objects.get(pk=data["resident_id"])
    return Appointment(**data)


def update_appointment(appointment, payload):
    data = normalize_payload(payload)
    for field, value in data.items():
        setattr(appointment, field, value)
    appointment.save()
    return appointment
