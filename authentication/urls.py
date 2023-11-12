from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.users),
    path("register/", views.register),
    path("login/", views.login),
]
