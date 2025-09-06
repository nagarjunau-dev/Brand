from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('admin/',views.admin,name=admin)
    path('register/',views.register_,name='register'),
    path('login/',views.login_,name='login'),
]
