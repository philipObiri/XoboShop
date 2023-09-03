from django.shortcuts import render, redirect
from .models import Product, PlaceOrder
from django.contrib import messages
from .form import PlaceOrderForm
from django.conf import settings
from payment.models import Payment


# Create your views here.
def homepage(request):
    return render(request, "product/index.html")


def place_order(request):
    # messages.success(request, "The details you give will help us deliver right")
    if request.method == "POST":
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            product = Product.objects.get(pk=1)  # the product in the database
            var.product = product
            var.user = request.user
            var.total_cost = product.price * var.item_amount
            var.save()
            payment = Payment.objects.create(
                amount=var.total_cost, email=request.user.email, user=request.user
            )
            payment.save()
            pk = settings.PAYSTACK_PUBLIC_KEY
            context = {
                "total_cost": var.total_cost,
                "item_amount": var.item_amount,
                "payment": payment,
                "paystack_public_key": pk,
                "amount_value": payment.amount_value(),
            }
            request.session["order_id"] = var.id
            return render(request, "product/make_payment.html", context)
        else:
            messages.warning(request, "Error, something went went")
            return redirect("place-order")

    else:
        form = PlaceOrderForm()
        context = {"form": form}
        return render(request, "product/place_order.html", context)
