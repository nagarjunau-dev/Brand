from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inx'),
    path('about/', views.about, name='about'),
    path('admin/',views.admin,name='admin'),
   
]
