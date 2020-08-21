from django.db import models
from django.contrib.auth.models import User
from kiosks.models import Kiosk
from customers.models import Customer

class  ProductSupplier(models.Model):
    GENDERS = (
        ("m", "male"),
        ("f", "female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    street_address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    date_added = models.DateField()
    id_number = models.IntegerField()
    profile_picture = models.ImageField()
    
    def __str__(self):
        return self.user.get_full_name()

class  ProductCategory(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField()

    def __str__(self):
        return self.name()


class Product(models.Model) :
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE )
    description = models.TextField()
    supplier_price = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2)
    selling_price = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2)
    supplier = models.ForeignKey(ProductSupplier,on_delete=models.CASCADE )
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE)
    number_in_stock = models.IntegerField()

    def __str__(self):
        return self.title()

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE )
    image = models.ImageField()

    def __str__(self):
        return self.product()



class ProductReview(models.Model) :  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    score = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.product()



    
   
