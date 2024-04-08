from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout, authenticate,login


from home.forms import clientForm,clientAddForm,vendorForm,vendorAddForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.models import Client,Vendor 
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import *

def homepage(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/landingpage.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
  
  
def register(request):
    return render(request,'account/register.html')

def registerClient(request):
    registered=False
    if request.method=='POST':
        var_clientForm=clientForm(request.POST)
        var_clientAddForm=clientAddForm(request.POST)
        if var_clientForm.is_valid() and var_clientAddForm.is_valid():
            clientprimary=var_clientForm.save()
            clientprimary.set_password(clientprimary.password)
            clientprimary.save()
            clientAdd=var_clientAddForm.save(commit=False)
            clientAdd.client=clientprimary
            clientAdd.save()
            registered=True
    else:
        var_clientForm=clientForm()
        var_clientAddForm=clientAddForm()
    return render(request,'Clients/Auth/registerclient.html',{'var_clientForm':var_clientForm,'var_clientAddForm':var_clientAddForm,'registered':registered})


def registerVendor(request):
    registered=False
    if request.method=='POST':
        var_vendorForm=vendorForm(request.POST)
        var_vendorAddForm=vendorAddForm(request.POST)
        if var_vendorForm.is_valid() and var_vendorAddForm.is_valid():
            vendorprimary=var_vendorForm.save()
            vendorprimary.set_password(vendorprimary.password)
            vendorprimary.save()
            vendorAdd=var_vendorAddForm.save(commit=False)
            vendorAdd.vendor=vendorprimary
            vendorAdd.save()
            registered=True
    else:
        var_vendorForm=vendorForm()
        var_vendorAddForm=vendorAddForm()
    return render(request,'Vendors/Auth/registerVendor.html',{'var_vendorForm':var_vendorForm,'var_vendorAddForm':var_vendorAddForm,'registered':registered})
    
def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                try:
                    current=Client.objects.get(client=request.user)
                except Client.DoesNotExist:
                    current=Vendor.objects.get(vendor=request.user)
                    try:
                        vendor = Vendor.objects.get(pk=id)
                    except Vendor.DoesNotExist:
                        vendor = None
                    try:
                        vendor = Vendor.objects.get(pk=id)
                    except Vendor.DoesNotExist:
                        vendor = None
                    if current.is_client:
                        return redirect('/clientDash/')
                    else:
                        return redirect('/vendorDash/')
                return render(request,'/dashboard.html')
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('pages/login/')
    else:
        return render(request,'pages/login.html',{'invalidlogin':invalidlogin})

# @login_required
def dashboard(request):
    try:
        current=Client.objects.get(client=request.user)
    except Client.DoesNotExist:
        current=Vendor.objects.get(vendor=request.user)
    if current.is_client:
        return redirect('/clientDash/')
    else:
        return redirect('/vendorDash/')
    return render(request,'/dashboard.html')

    

def clientDash(request):
    return render(request,'home/clientDash.html')

def vendorDash(request):
    return render(request,'home/vendorDash.html')
