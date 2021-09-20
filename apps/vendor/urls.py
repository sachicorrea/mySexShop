from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('se-un-vendor/', views.become_vendor, name='become_vendor'),
    path('vendedor-admin/', views.vendor_admin, name='vendor_admin'),
    path('agregar-producto/', views.add_product, name='add_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ingresar/',
         auth_views.LoginView.as_view(template_name='vendor/login.html'),
         name='login'),
]