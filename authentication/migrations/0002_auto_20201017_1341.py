# Generated by Django 3.1 on 2020-10-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_vendor',
        ),
    ]
