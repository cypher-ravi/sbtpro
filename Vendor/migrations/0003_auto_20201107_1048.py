# Generated by Django 3.1 on 2020-11-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0002_auto_20201107_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='Vendor.KeyWord'),
        ),
    ]
