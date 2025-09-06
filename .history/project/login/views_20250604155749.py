from django.shortcuts import render
from . models import Product


# Create your views here.
def home(request):
    all_products = Product.objects.all()
    return render(request, 'index.html',{'all_products':all_products})

def pdp(request,id):
    product = Product.objects.all(id=id)
    return render(request, 'description.html',{'product':product})

def about(request):
    return render(request, 'about.html')

def admin(request):
    return render(request,'admin.html')

def profile(request):
    return render(request,'profile.html')


