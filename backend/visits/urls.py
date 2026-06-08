from django.urls import path

from . import views


urlpatterns = [
    path("", views.visits_collection),
    path("<int:pk>/", views.visit_detail),
]
