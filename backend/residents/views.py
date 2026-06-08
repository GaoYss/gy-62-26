from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backend.common.http import error, list_response, ok, parse_json

from .models import Resident
from .services import create_resident, list_residents, serialize_resident, update_resident


@csrf_exempt
@require_http_methods(["GET", "POST", "OPTIONS"])
def residents_collection(request):
    if request.method == "GET":
        return list_response(list_residents())

    try:
        resident = create_resident(parse_json(request))
        resident.full_clean()
        resident.save()
        return ok(serialize_resident(resident), status=201)
    except (ValidationError, IntegrityError, TypeError, ValueError) as exc:
        return error(str(exc))


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE", "OPTIONS"])
def resident_detail(request, pk):
    resident = get_object_or_404(Resident, pk=pk)

    if request.method == "GET":
        return ok(serialize_resident(resident))

    if request.method == "DELETE":
        resident.delete()
        return ok({"deleted": True})

    try:
        resident = update_resident(resident, parse_json(request))
        resident.full_clean()
        resident.save()
        return ok(serialize_resident(resident))
    except (ValidationError, IntegrityError, TypeError, ValueError) as exc:
        return error(str(exc))
