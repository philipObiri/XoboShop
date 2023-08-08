from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("place-order/", views.place_order, name="place-order"),
]
