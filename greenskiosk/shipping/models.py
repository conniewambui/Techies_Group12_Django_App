from django.db import models
from django.contrib.auth.models import User
from shopping.models import Order
from catalogue.models import Product


class ShippingProvider (models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    transport_mode = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()
    

class DispenserCoolerBox (models.Model):
    box_number = models.IntegerField()   
    location = models.CharField(max_length=100)
    unlock_code = models.IntegerField()

    def __str__(self):
        return self.box_number()


class  Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    shipping_provider = models.ForeignKey(ShippingProvider, on_delete=models.CASCADE)
    cooler_box = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.order()

