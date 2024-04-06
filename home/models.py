from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200, default=False)
    type_of_software = models.CharField(max_length=200, default=False)
    vendor_id = models.PositiveIntegerField(default=False)
    website = models.CharField(max_length=50, default=False)
    product_category = models.CharField(max_length=50, default=False)
    description = models.CharField(max_length=500, default=False)
    software_name = models.CharField(max_length=50, default=False)
    business_areas = models.CharField(max_length=200, default=False)
    modules = models.CharField(max_length=50, default=False)
    financial_services_client_types = models.CharField(max_length=100, default=False)
    cloud_options = (
        ('cloud_native', 'cloud_native'),
        ('cloud_based', 'cloud_based'),
        ('cloud_enabled', 'cloud_enabled'),
    )
    cloud_type=models.CharField(
        max_length=200,
        choices=cloud_options,
        blank=True,
        null=True
    )
    additional_info = models.CharField(max_length=500, default=False)
    
    def __str__(self):
        return self.company_name
    
    
    
class Client(models.Model):
    client=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200, default=False)
    address = models.CharField(max_length=100, default=False)
    country = models.CharField(max_length=500)
    nationality = models.CharField(max_length=500)
    email = models.EmailField(('email address'), unique=True, default=False)
    is_client=models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.client.username 
    
    
    
class Vendor(models.Model):
    vendor=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default=False)
    location_countries = models.CharField(max_length=500)
    company_established = models.PositiveIntegerField(default=False)
    location_cities = models.CharField(max_length=100)
    contact_telephone_no = models.CharField(max_length=200, default=False)
    no_of_employees = models.PositiveIntegerField(default=False)
    internal_professional_services = models.CharField(max_length=3, default=False)
    last_demo_date = models.CharField(max_length=20, default=False)
    last_reviewed_date = models.CharField(max_length=20, default=False)
    document_to_attach = models.FileField(max_length=3, default=False)
    
    def __str__(self):
        return self.vendor.username 
    

   