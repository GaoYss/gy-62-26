import json

from django.http import JsonResponse


def parse_json(request):
    if not request.body:
        return {}
    return json.loads(request.body.decode("utf-8"))


def ok(data=None, status=200):
    return JsonResponse(data or {}, status=status, json_dumps_params={"ensure_ascii": False})


def list_response(items):
    return ok({"results": items})


def error(message, status=400):
    return ok({"error": message}, status=status)
