from django.contrib import admin
from . import models
from .models import Addres
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = models.Product
    list_display=['id','name','price','desc','image']



class CartAdmin(admin.ModelAdmin):
    model = models.Cart
    list_display=['id','name','price','desc','image','quantity','total_price','host']

admin.site.register(models.Cart,CartAdmin)

class AddresAdmin(admin.ModelAdmin):
    model = models.Addres
    list_display=['id','addresstype','fullname','phonenumber','pincode','email','deliveryaddress','host']

admin.site.register(models.Addres,AddresAdmin)