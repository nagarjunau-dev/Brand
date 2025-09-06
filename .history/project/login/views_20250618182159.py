from django.shortcuts import render,redirect,get_object_or_404
from . models import Product,Cart,Addres
from django.contrib.auth.decorators import login_required
from django.db.models import Q





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
        count = Cart.objects.filter(host=request.user).count()
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



# def remove_from_cart(request, id):
#     cart_item = get_object_or_404(Cart, id=id, host=request.user)
#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.total_price -= cart_item.price
#         cart_item.save()
#     else:
#         cart_item.delete()
#     return redirect('cart')  # replace with your cart page URL name

def remove_cart(request,id):
    Cart.objects.get(id=id).delete()
    return redirect('cart')


def checkout(request):
    cart_products=Cart.objects.filter(host=request.user)
    product_total=sum(item.total_price for item in cart_products)
    total_quantity=sum(item.quantity for item in cart_products)
    gst=0.8
    shipping_charges=10
    gst_amt = product_total *gst/100
    total_price = product_total + gst_amt + shipping_charges
    return render(request,'checkout.html',
                {"cart_products":cart_products,
                "product_total":product_total,
                "total_quantity":total_quantity,
                "shipping_charges":shipping_charges,
                "gst_amt":gst_amt,
                "total_price":total_price})

def search_view(request):
    query = request.GET.get('search')
    if query:
        result = Product.objects.filter(
            Q(name__icontains=query) | Q(desc__icontains=query)
        )
    else:
        result = Product.objects.all()
    return render(request,'index.html',{'result':result})

def thankyou(request):
    useraddress = Addres.objects.all()
    return render(request,'thankyou.html',{'useraddress':useraddress})

def user_details(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            addresstype = request.POST['addresstype']
            fullname = request.POST['fullname']
            phonenumber = request.POST['contactnumber']
            pincode = request.POST['pincode']
            email = request.POST['email']
            deliveryaddress = request.POST['address']
            
            Addres.objects.create(addresstype=addresstype,
                                   fullname=fullname,
                                   phonenumber=phonenumber,
                                   pincode=pincode,
                                   email=email,
                                   deliveryaddress=deliveryaddress,
                                   host=request.user)
            return redirect('thankyou')
    return render(request,'checkout.html')