from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='home'

urlpatterns = [
  path('', views.homepage,  name='homepage'),
  path('tables/', views.tables, name='tables'),
  # path('',views.dashboard,name='index'),
  path('register/',views.register,name='register'),
  path('registerClient/',views.registerClient,name='registerClient'),
  path('registerVendor/',views.registerVendor,name='registerVendor'),
  path('login/',views.userLogin,name='userLogin'),
]
