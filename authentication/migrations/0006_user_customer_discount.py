# Generated by Django 3.1 on 2020-11-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20201017_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='customer_discount',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
