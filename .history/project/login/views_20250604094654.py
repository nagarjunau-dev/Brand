from django.shortcuts import render


# Create your views here.
def home(request):
    all_products = Products.objects.all()
    return render(request, 'index.html',{'all_products;'})

def about(request):
    return render(request, 'about.html')

def admin(request):
    return render(request,'admin.html')

def profile(request):
    return render(request,'profile.html')


