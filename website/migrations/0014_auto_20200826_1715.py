# Generated by Django 3.0.8 on 2020-08-26 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_vendor_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
