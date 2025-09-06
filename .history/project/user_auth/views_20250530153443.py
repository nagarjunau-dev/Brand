from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
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
    if request.method == 'POST': 
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'bool':True})
    
    return render(request,'login.html')


def logout_()