# Generated by Django 3.1 on 2020-11-03 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0015_vendorservices_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorservices',
            old_name='Vendor',
            new_name='vendor',
        ),
    ]
