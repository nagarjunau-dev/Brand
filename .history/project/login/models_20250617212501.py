from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to='uploads')
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    host = models.ForeignKey(to=User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class Address(models.Model):
    addresstype = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    pincode = models.IntegerField()
    email = models.TextField()
    deliveryaddress = models.TextField()
    host = models.ForeignKey(to=User,on_delete=models.CASCADE,null=true)

    # def deliveryaddr(self):
    #     return self.deliveryaddr






