# Generated by Django 3.1 on 2020-10-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_auto_20201019_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
