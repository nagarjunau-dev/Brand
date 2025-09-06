from django.shortcuts import render,redirect
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

def addtocart(request,id):
    product = Product.objects.get(id=id)
    cart.objects.create(name=p.name,price=p.price,desc=p.desc,image=p.image,total_price=p.price,host=request)
    return redirect('cart')
    
def admin(request):
    return render(request,'admin.html')

def profile(request):
    return render(request,'profile.html')


