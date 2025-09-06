from django.shortcuts import render,redirect
from . models import Product,Cart
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
    if request.user.is_authenticated:
        cart_products=Cart.objects.filter(host=request.user)
        coun
    return render(request, 'cart.html',{"cart_products":cart_products})

def addtocart(request,id):
    p = Product.objects.get(id=id)
    try:
        x=Cart.objects.get(host=request.user, name=p.name)
        x.quantity += 1
        x.total_price +=p.price
        x.save()
    except:
        cart_obj= Cart.objects.create(name=p.name,price=p.price,desc=p.desc,image=p.image,total_price=p.price,host=request.user)
        cart_obj.save()
    return redirect('cart')
    
def admin(request):
    return render(request,'admin.html')

def profile(request):
    return render(request,'profile.html')


