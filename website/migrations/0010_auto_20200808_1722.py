# Generated by Django 3.0.8 on 2020-08-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200808_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
