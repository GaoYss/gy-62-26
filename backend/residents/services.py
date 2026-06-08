from .models import Resident


FIELDS = [
    "id",
    "name",
    "gender",
    "age",
    "room_number",
    "care_level",
    "emergency_contact",
    "emergency_phone",
    "medical_notes",
    "created_at",
    "updated_at",
]


def serialize_resident(resident):
    return {
        "id": resident.id,
        "name": resident.name,
        "gender": resident.gender,
        "age": resident.age,
        "room_number": resident.room_number,
        "care_level": resident.care_level,
        "emergency_contact": resident.emergency_contact,
        "emergency_phone": resident.emergency_phone,
        "medical_notes": resident.medical_notes,
        "created_at": resident.created_at.isoformat(),
        "updated_at": resident.updated_at.isoformat(),
    }


def list_residents():
    return [serialize_resident(item) for item in Resident.objects.all()]


def create_resident(payload):
    data = {field: payload.get(field) for field in FIELDS if field in payload}
    data.pop("id", None)
    data.pop("created_at", None)
    data.pop("updated_at", None)
    return Resident(**data)


def update_resident(resident, payload):
    for field in FIELDS:
        if field not in {"id", "created_at", "updated_at"} and field in payload:
            setattr(resident, field, payload[field])
    resident.save()
    return resident
