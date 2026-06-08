from django.urls import path

from . import views


urlpatterns = [
    path("", views.appointments_collection),
    path("<int:pk>/", views.appointment_detail),
]
