# Generated by Django 3.1 on 2020-11-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20201109_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, null=True, verbose_name='password'),
        ),
    ]