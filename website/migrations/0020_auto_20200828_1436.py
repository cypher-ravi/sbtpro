# Generated by Django 3.0.8 on 2020-08-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20200828_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Service_decsription',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
