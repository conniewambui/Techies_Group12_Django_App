from django.contrib import admin

# Register your models here.
from .models import ShippingProvider, DispenserCoolerBox, Delivery
admin.site.register(DispenserCoolerBox)
admin.site.register(Delivery)
admin.site.register(ShippingProvider)
