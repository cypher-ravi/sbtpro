# Generated by Django 3.1 on 2020-09-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_merge_20200930_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plan_img',
            field=models.ImageField(default='', upload_to='website/membershipcard'),
        ),
    ]