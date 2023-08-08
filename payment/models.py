from django.db import models
import secrets
from payment.paystack import Paystack
from django.contrib.auth.models import User

# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    reference = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} paid {self.amount} GHS on {self.timestamp.date()} at exactly {self.timestamp.time()}"

    def save(self, *args, **kwargs):
        while not self.reference:
            reference = secrets.token_urlsafe(
                50
            )  # generate a unique id made up of 50 random characters
            object_with_similar_reference = Payment.objects.filter(reference=reference)
            if not object_with_similar_reference:
                self.reference = reference
        super().save(*args, **kwargs)

    # When you have a value (in any currency) you first need to multiply it by 100 to get the base value of the currency
    def amount_value(self):
        return int(self.amount) * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.reference, self.amount)
        if status:
            if result["amount"] / 100 == self.amount:
                self.verified = True
                self.save()
        if self.verified:
            return True
        else:
            return False
