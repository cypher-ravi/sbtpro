# Generated by Django 3.0.8 on 2020-08-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_servicecontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecontact',
            name='regsitrant_interest',
            field=models.CharField(default='', max_length=50),
        ),
    ]
