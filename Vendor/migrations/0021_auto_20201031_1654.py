# Generated by Django 3.1 on 2020-10-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0020_vendor_registration_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='website/images/vendors'),
        ),
    ]
