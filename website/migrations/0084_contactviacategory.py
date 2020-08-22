# Generated by Django 3.0.8 on 2020-08-22 19:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0083_sub_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactviacategory',
            fields=[
                ('registrant_id', models.AutoField(primary_key=True, serialize=False)),
                ('registrant_name', models.CharField(default='', max_length=50)),
                ('registrant_mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('calling_time', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
