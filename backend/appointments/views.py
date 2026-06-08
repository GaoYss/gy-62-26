from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.common.http import error, list_response, ok, parse_json

from .models import Appointment
from .services import create_appointment, list_appointments, serialize_appointment, update_appointment


@csrf_exempt
@require_http_methods(["GET", "POST", "OPTIONS"])
def appointments_collection(request):
    if request.method == "GET":
        return list_response(list_appointments(request.GET.get("status")))

    try:
        appointment = create_appointment(parse_json(request))
        appointment.full_clean()
        appointment.save()
        return ok(serialize_appointment(appointment), status=201)
    except (ObjectDoesNotExist, ValidationError, IntegrityError, KeyError, TypeError, ValueError) as exc:
        return error(str(exc))


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE", "OPTIONS"])
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment.objects.select_related("resident"), pk=pk)

    if request.method == "GET":
        return ok(serialize_appointment(appointment))

    if request.method == "DELETE":
        appointment.delete()
        return ok({"deleted": True})

    try:
        appointment = update_appointment(appointment, parse_json(request))
        appointment.full_clean()
        appointment.save()
        return ok(serialize_appointment(appointment))
    except (ObjectDoesNotExist, ValidationError, IntegrityError, TypeError, ValueError) as exc:
        return error(str(exc))
