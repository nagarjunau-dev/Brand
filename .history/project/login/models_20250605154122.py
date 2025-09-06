from django.db import models

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
    total_price = models.IntegerField(default=0)


