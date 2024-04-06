# Generated by Django 4.2.9 on 2024-03-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='location_cities',
        ),
        migrations.RemoveField(
            model_name='product',
            name='info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='additional_info',
            field=models.CharField(default=False, max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='business_areas',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='cloud_type',
            field=models.CharField(blank=True, choices=[('cloud_native', 'cloud_native'), ('cloud_based', 'cloud_based'), ('cloud_enabled', 'cloud_enabled')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_established',
            field=models.PositiveIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='company_name',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='contact_telephone_no',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=False, max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='financial_services_client_types',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='internal_professional_services',
            field=models.CharField(default=False, max_length=3),
        ),
        migrations.AddField(
            model_name='product',
            name='last_demo_date',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='last_reviewed_date',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='modules',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='no_of_employees',
            field=models.PositiveIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='software_name',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='type_of_software',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor_id',
            field=models.PositiveIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='website',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
