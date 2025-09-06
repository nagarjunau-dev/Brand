from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def admin(request):
    return render(request,'admin.html')

def register_(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname=request.POST['lastname']
        username =request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user=User.objects.create(request,
                firstname=firstname,
                lastname=lastname,
                username=username,
                email=email)                
        user.save()
        return redirect('login')

    return render(request,'register.html')

def login_(request):
    return render(request,'login.html')
