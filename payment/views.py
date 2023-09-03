from django.shortcuts import render, redirect
from django.conf import settings
from product.models import PlaceOrder
from payment.models import Payment
from django.contrib import messages


def verify_payment(request, ref):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verify_payment()

    if verified:
        pk = request.session["order_id"]
        order = PlaceOrder.objects.get(pk=pk)
        order.is_verified = True
        order.save()
        context = {
            "payment": payment,
            "placed_order": pk,
        }
        return render(request, "product/success.html")

    else:
        messages.error("Sorry your order was not processed. Please contact Support")
        return redirect("place-order")
