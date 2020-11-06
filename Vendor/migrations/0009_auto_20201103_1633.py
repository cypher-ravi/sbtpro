# Generated by Django 3.1 on 2020-11-03 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0008_vendorimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorimages',
            name='vendor',
        ),
        migrations.AddField(
            model_name='vendorimages',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vendor.vendor'),
        ),
    ]