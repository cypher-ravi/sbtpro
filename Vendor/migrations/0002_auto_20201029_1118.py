# Generated by Django 3.1 on 2020-10-29 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
        ('Vendor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='Busniess_Type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.categories'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_images',
            field=models.ManyToManyField(blank=True, to='Vendor.VendorImages'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_services',
            field=models.ManyToManyField(blank=True, to='Vendor.VendorServices'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vendor.vendorvideos'),
        ),
    ]
