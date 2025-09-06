from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('addtocart/',views.)
    path('admin/',views.admin,name='admin'),
    path('profile/',views.profile,name='profile'),
    path('description/<int:id>',views.pdp,name='description'),
   
]
