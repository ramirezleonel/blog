from django.urls import path

from . import views

urlpatterns = [
    path("", views.bienvenida, name="index"),
    path("/login", views.login, name="login"),
]