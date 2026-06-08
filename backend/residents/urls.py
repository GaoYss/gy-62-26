from django.urls import path

from . import views


urlpatterns = [
    path("", views.residents_collection),
    path("<int:pk>/", views.resident_detail),
]
