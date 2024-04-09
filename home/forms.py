from django import forms
from django.contrib.auth.models import User
from home.models import Client,Vendor

class clientForm(forms.ModelForm):
    password=forms.PasswordInput(attrs={'class':'form-control'})
    class Meta():
        model=User
        fields=('first_name','last_name','username','email','password')
        
        widgets = {
                    'first_name':forms.TextInput(attrs={'class': 'form-control'}),
                    'last_name':forms.TextInput(attrs={'class': 'form-control'}),
                    'username':forms.TextInput(attrs={'class': 'form-control'}),
                    'email':forms.EmailInput(attrs={'class': 'form-control'}),
                    'password':forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class clientAddForm(forms.ModelForm):
    class Meta():
        model=Client
        fields=('phone_number','address', 'country', 'nationality')
        
        widgets = {
                    'phone_number':forms.TextInput(attrs={'class': 'form-control'}),
                    'address':forms.TextInput(attrs={'class': 'form-control'}),
                    'country':forms.TextInput(attrs={'class': 'form-control'}),
                    'nationality':forms.TextInput(attrs={'class': 'form-control'}),
        }

class vendorForm(forms.ModelForm):
    password=forms.PasswordInput(attrs={'class':'form-control'})
    class Meta():
        model=User
        fields=('first_name','last_name','username','email','password')
        widgets = {
                    'first_name':forms.TextInput(attrs={'class': 'form-control'}),
                    'last_name':forms.TextInput(attrs={'class': 'form-control'}),
                    'username':forms.TextInput(attrs={'class': 'form-control'}),
                    'email':forms.EmailInput(attrs={'class': 'form-control'}),
                    'password':forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class vendorAddForm(forms.ModelForm):
    class Meta():
        model=Vendor
        fields=('company_name','address','location_countries', 'company_established', 'location_cities', 'contact_telephone_no', 'no_of_employees', 'internal_professional_services', 'last_demo_date', 'last_reviewed_date', 'document_to_attach')
        widgets = {
                    'address':forms.TextInput(attrs={'class': 'form-control'}),
                    'company_name':forms.TextInput(attrs={'class': 'form-control'}),
                    'location_countries':forms.TextInput(attrs={'class': 'form-control'}),
                    'company_established':forms.TextInput(attrs={'class': 'form-control'}),
                    'contact_telephone_no':forms.TextInput(attrs={'class': 'form-control'}),
                    'location_cities':forms.TextInput(attrs={'class': 'form-control'}),
                    'no_of_employees':forms.TextInput(attrs={'class': 'form-control'}),
                    'internal_professional_services':forms.TextInput(attrs={'class': 'form-control'}),
                    'last_demo_date':forms.TextInput(attrs={'class': 'form-control'}),
                    'last_reviewed_date':forms.TextInput(attrs={'class': 'form-control'}),
                    # 'cloud_type' :forms.ChoiceField(choices=cloud_options, widget=forms.Select(attrs={'class':'form-control'})),
                    # 'document_to_attach':forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
        }


        