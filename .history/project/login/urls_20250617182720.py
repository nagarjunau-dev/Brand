from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('admin/',views.admin,name='admin'),
    path('profile/',views.profile,name='profile'),
    path('description/<int:id>',views.pdp,name='description'),
    path('remove_cart/<int:id>/', views.remove_cart, name='remove_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('search/',views.search_view,name='search'),
    path('thankyou/',views.thankyou,)
   
]
