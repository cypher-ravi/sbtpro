# Generated by Django 3.0.8 on 2020-08-18 17:09

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0047_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryContacts',
            fields=[
                ('query_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]