from django.shortcuts import render, redirect
from django.conf import settings
from product.models import PlaceOrder
from .models import Payment
from django.contrib import messages


# Create your views here.
def verify_payment(request, reference):
    payment = Payment.objects.get(reference=reference)
    verified = payment.verify_payment()
    if verified:
        pk = request.session["order_id"]
        order = PlaceOrder.objects.get(pk=pk)
        if order:
            order.is_verified = True
        order.save()
        context = {
            "placed_order": pk,
            "payment": payment,
        }
        return render(request, "success.html", context)
    else:
        messages.warning(
            request,
            "Sorry , your order was not processed. Please contact Zobo Shop Support ",
        )
        return redirect("place-order")
