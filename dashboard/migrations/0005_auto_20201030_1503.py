# Generated by Django 3.1 on 2020-10-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_branchreport_submit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchreport',
            name='submit_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
