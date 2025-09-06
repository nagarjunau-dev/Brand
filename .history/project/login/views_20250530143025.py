from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def admin(request):
    return render(request,'admin.html')

def register_(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name=request.POST['lastname']
        username =request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user=User.objects.create(request,
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email)
        user.set_password(password)                
        user.save()
        return redirect('login')

    return render(request,'register.html')

def login_(request):
    username=request.POST['username']
    password=request.POST['password']
    user= authenticate(request,username=username, pas)
    return render(request,'login.html')
