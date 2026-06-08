from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.common.http import error, list_response, ok, parse_json

from .models import EmergencyNotification
from .services import create_notification, list_notifications, serialize_notification, update_notification


@csrf_exempt
@require_http_methods(["GET", "POST", "OPTIONS"])
def notifications_collection(request):
    if request.method == "GET":
        active = request.GET.get("active")
        active_value = None if active is None else active.lower() == "true"
        return list_response(list_notifications(active_value))

    try:
        notification = create_notification(parse_json(request))
        notification.full_clean()
        notification.save()
        return ok(serialize_notification(notification), status=201)
    except (ValidationError, IntegrityError, TypeError, ValueError) as exc:
        return error(str(exc))


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE", "OPTIONS"])
def notification_detail(request, pk):
    notification = get_object_or_404(EmergencyNotification, pk=pk)

    if request.method == "GET":
        return ok(serialize_notification(notification))

    if request.method == "DELETE":
        notification.delete()
        return ok({"deleted": True})

    try:
        notification = update_notification(notification, parse_json(request))
        notification.full_clean()
        notification.save()
        return ok(serialize_notification(notification))
    except (ValidationError, IntegrityError, TypeError, ValueError) as exc:
        return error(str(exc))
