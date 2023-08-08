from django import forms
from .models import PlaceOrder


class PlaceOrderForm(forms.ModelForm):
    class Meta:
        model = PlaceOrder
        fields = ["full_name", "item_amount", "delivery_address", "phone_number"]
