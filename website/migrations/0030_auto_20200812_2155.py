# Generated by Django 3.0.8 on 2020-08-12 21:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_auto_20200812_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top',
            name='vendor_mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
