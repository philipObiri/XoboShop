from django.urls import path
from . import views

urlpatterns = [
    path("verify-payment/<str:ref>", views.verify_payment, name="verify_payment")
]
