# Generated by Django 4.2.9 on 2024-04-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_vendor_is_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='document_to_attach',
            field=models.FileField(blank=True, default=None, max_length=3, null=True, upload_to=''),
        ),
    ]
