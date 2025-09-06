from django.shortcuts import render
from . models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    all_products = Product.objects.all()
    return render(request, 'index.html',{'all_products':all_products})

def pdp(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'description.html',{'product':product})

@login_required(login_url='login')
def cart(request):
    return render(request, 'cart.html')

def addtocart(r)

def admin(request):
    return render(request,'admin.html')

def profile(request):
    return render(request,'profile.html')


