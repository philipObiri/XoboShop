from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name
    
    

class PlaceOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.Case)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    item_amount = models.PositiveIntegerField(default=1)
    total_cost = models.PositiveIntegerField()
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)
    
    # let's say a customer makes an order and pays . We would like to verify  the payment
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user} ordered for {self.product}"
