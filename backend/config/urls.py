from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def health(_request):
    return JsonResponse({"status": "ok", "service": "elder-care-visits"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health),
    path("api/residents/", include("backend.residents.urls")),
    path("api/appointments/", include("backend.appointments.urls")),
    path("api/visits/", include("backend.visits.urls")),
    path("api/notifications/", include("backend.notifications.urls")),
]
