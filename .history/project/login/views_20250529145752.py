from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
