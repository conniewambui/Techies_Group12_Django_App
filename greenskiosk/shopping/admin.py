from django.contrib import admin

# Register your models here.
from .models import Cart, Payment, Order
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Order)
