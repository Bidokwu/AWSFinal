from django import forms
from django.contrib.auth.models import User
from home.models import Client,Vendor

class clientForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']


class clientAddForm(forms.ModelForm):
    class Meta():
        model=Client
        fields=['phone_number','address', 'country', 'nationality']

class vendorForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']



class vendorAddForm(forms.ModelForm):
    class Meta():
        model=Vendor
        fields=['address','location_countries', 'company_established', 'location_cities', 'contact_telephone_no', 'no_of_employees', 'internal_professional_services', 'last_demo_date', 'last_reviewed_date', 'document_to_attach']


        