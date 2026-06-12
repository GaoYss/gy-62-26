from django.urls import path

from . import views


urlpatterns = [
    path("", views.appointments_collection),
    path("config/", views.appointment_config),
    path("<int:pk>/", views.appointment_detail),
]
