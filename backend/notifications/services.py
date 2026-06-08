from .models import EmergencyNotification


FIELDS = ["title", "content", "level", "target_group", "is_active"]


def serialize_notification(notification):
    return {
        "id": notification.id,
        "title": notification.title,
        "content": notification.content,
        "level": notification.level,
        "target_group": notification.target_group,
        "is_active": notification.is_active,
        "published_at": notification.published_at.isoformat(),
        "updated_at": notification.updated_at.isoformat(),
    }


def list_notifications(active=None):
    queryset = EmergencyNotification.objects.all()
    if active is not None:
        queryset = queryset.filter(is_active=active)
    return [serialize_notification(item) for item in queryset]


def create_notification(payload):
    data = {field: payload.get(field) for field in FIELDS if field in payload}
    return EmergencyNotification(**data)


def update_notification(notification, payload):
    for field in FIELDS:
        if field in payload:
            setattr(notification, field, payload[field])
    notification.save()
    return notification
