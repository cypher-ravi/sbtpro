# Generated by Django 3.1 on 2020-10-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0038_auto_20201031_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorimages',
            name='title',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
