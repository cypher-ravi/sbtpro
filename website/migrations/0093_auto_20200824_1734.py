# Generated by Django 3.0.8 on 2020-08-24 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0092_auto_20200824_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactviacategory',
            name='service_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Subcategory'),
        ),
    ]
