# Generated by Django 3.1 on 2020-11-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20201102_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='customer_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
