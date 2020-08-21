from django.db import models
from django.contrib.auth.models import User
from catalogue.models import Product
from customers.models import Customer


# Create your models here.

class Cart(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    total_price = models.DecimalField(blank=True, null=True, max_digits=2000, decimal_places=10)
    status = models.CharField(max_length=100)

    def __str__(self):
       return self.cart()


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    #order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=10)
    date_of_payment = models.DateTimeField()

    def __str__(self):
        return self.customer()


class Order(models.Model) :
    order_number = models.IntegerField()
    date_placed = models.DateTimeField()
    status = models.CharField(max_length=100)
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    shipping_provider = models.ForeignKey('shipping.ShippingProvider', on_delete=models.CASCADE)
    order_price = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2)
    shipping_cost = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2)
    total_price = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_number()
