# Generated by Django 3.1 on 2020-10-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_auto_20201020_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, default='Please Select', max_length=100, null=True),
        ),
    ]