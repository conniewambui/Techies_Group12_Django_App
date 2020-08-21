from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer (models.Model)   :
    GENDERS = (
        ("m", "male"),
        ("f", "female")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    gender = models.CharField(max_length=6, choices=GENDERS)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.user.get_full_name()


class ShippingAddress (models.Model) :
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE )  
    address = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.customer()


