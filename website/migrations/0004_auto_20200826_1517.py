# Generated by Django 3.0.8 on 2020-08-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200826_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelisting',
            name='mobile',
            field=models.IntegerField(default='', max_length=12),
        ),
    ]
