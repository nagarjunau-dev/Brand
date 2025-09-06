from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def admin(request):
    return render(request,'admin.html')


