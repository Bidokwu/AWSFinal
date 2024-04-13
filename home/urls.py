from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='home'

urlpatterns = [
  path('', views.homepage,  name='homepage'),
  path('tables/', views.tables, name='tables'),
  path('client_tables/', views.client_tables, name='client_tables'),
  path('vendor_tables/', views.vendor_tables, name='vendor_tables'),
  path('dashboard/',views.dashboard,name='index'),
  path('register/',views.register,name='register'),
  
  path('registerVendor/',views.registerVendor,name='registerVendor'),
  path('registerClient/',views.registerClient,name='registerClient'),
  
  # Multiuser Dashboards 
  path('vendor/',views.vendorDash,name='vendorDash'),
  path('client/',views.clientDash,name='clientDash'),
  
  path('login/',views.userLogin,name='userLogin'),
]
