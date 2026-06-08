from django.urls import path

from . import views


urlpatterns = [
    path("", views.notifications_collection),
    path("<int:pk>/", views.notification_detail),
]
