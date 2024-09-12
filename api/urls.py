from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("csrf", views.get_csrf_token, name="csrf_token"),
    path("host/command", views.host_command, name="host_command"),
]