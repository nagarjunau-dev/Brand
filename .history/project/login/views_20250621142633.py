from django.shortcuts import render,redirect,get_object_or_404
from . models import Product,Cart,Addres
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages





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
    return render(request, 'cart.html',{"cart_products":cart_products,"count":count})

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
    gst_amt = product_total * (gst/100)
    total_price = product_total + gst_amt + shipping_charges
    return render(request,'checkout.html',{
        "cart_products":cart_products,
        "product_total":product_total,
        "total_quantity":total_quantity,
        "shipping_charges":shipping_charges,
        "gst_amt":gst_amt,
        "total_price":total_price
    })

def search_view(request):
    query = request.GET.get('searched',)
    if query:
        result = Product.objects.filter(
            Q(name__icontains=query) | Q(desc__icontains=query)
        )
    else:
        result = Product.objects.all()
    return render(request,'index.html',{'query': True,'result':result})

def thankyou(request,address_id):
    useraddress = Addres.objects.get(id=address_id,host=request.user)
    return render(request,'thankyou.html',{'useraddress':useraddress})

# def user_details(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             try:
#                 addresstype = request.POST['addresstype']
#                 fullname = request.POST['fullname']
#                 phonenumber = request.POST['contactnumber']
#                 pincode = request.POST['pincode']
#                 email = request.POST['email']
#                 deliveryaddress = request.POST['address']
                
#                 new_address=Addres.objects.create(addresstype=addresstype,
#                                     fullname=fullname,
#                                     phonenumber=phonenumber,
#                                     pincode=pincode,
#                                     email=email,
#                                     deliveryaddress=deliveryaddress,
#                                     host=request.user)
#                 return redirect('thankyou', address_id=new_address.id)
#             except Exception as e:
#                 print(e)
#     return render(request,'checkout.html')



def user_details(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                addresstype = request.POST['addresstype']
                fullname = request.POST['fullname']
                phonenumber = request.POST['contactnumber']
                pincode = request.POST['pincode']
                email = request.POST['email']
                deliveryaddress = request.POST['address']

                # Try to get an existing address with the same details
                try:
                    address_obj = Addres.objects.get(
                        host=request.user,
                        fullname=fullname,
                        phonenumber=phonenumber,
                        pincode=pincode,
                        email=email,
                        deliveryaddress=deliveryaddress,
                        addresstype=addresstype
                    )
                    # Optionally update or notify if already exists
                    messages.info(request, "Address already exists.")
                except Addres.DoesNotExist:
                    # If not found, create new
                    address_obj = Addres.objects.create(
                        addresstype=addresstype,
                        fullname=fullname,
                        phonenumber=phonenumber,
                        pincode=pincode,
                        email=email,
                        deliveryaddress=deliveryaddress,
                        host=request.user
                    )
                    messages.success(request, "New address added successfully.")

                return redirect('thankyou', address_id=address_obj.id)

            except KeyError as e:
                messages.error(request, f"Missing form field: {e}")
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")

    return render(request, 'checkout.html')
