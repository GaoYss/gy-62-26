from django.utils.dateparse import parse_datetime

from backend.appointments.models import Appointment
from backend.appointments.services import serialize_appointment

from .models import VisitRecord


WRITE_FIELDS = [
    "appointment",
    "appointment_id",
    "check_in_time",
    "check_out_time",
    "visitor_temperature",
    "staff_name",
    "summary",
]


def serialize_visit(record):
    return {
        "id": record.id,
        "appointment": serialize_appointment(record.appointment),
        "appointment_id": record.appointment_id,
        "check_in_time": record.check_in_time.isoformat(),
        "check_out_time": record.check_out_time.isoformat() if record.check_out_time else None,
        "visitor_temperature": str(record.visitor_temperature) if record.visitor_temperature is not None else "",
        "staff_name": record.staff_name,
        "summary": record.summary,
        "created_at": record.created_at.isoformat(),
        "updated_at": record.updated_at.isoformat(),
    }


def normalize_payload(payload):
    data = {field: payload.get(field) for field in WRITE_FIELDS if field in payload}
    if "appointment" in data:
        data["appointment_id"] = data.pop("appointment")
    for key in ["check_in_time", "check_out_time"]:
        if key in data and isinstance(data[key], str) and data[key]:
            data[key] = parse_datetime(data[key])
    if data.get("check_out_time") == "":
        data["check_out_time"] = None
    return data


def list_visits():
    queryset = VisitRecord.objects.select_related("appointment", "appointment__resident")
    return [serialize_visit(item) for item in queryset]


def create_visit(payload):
    data = normalize_payload(payload)
    Appointment.objects.get(pk=data["appointment_id"])
    return VisitRecord(**data)


def update_visit(record, payload):
    data = normalize_payload(payload)
    for field, value in data.items():
        setattr(record, field, value)
    record.save()
    return record
