from django.urls import path
from . import views

urlpatterns = [
    path("", views.getData),
    path("add-item/", views.addItem),
    path("item/<int:id>", views.getItem),
]
