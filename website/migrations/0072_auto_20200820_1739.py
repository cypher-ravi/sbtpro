# Generated by Django 3.0.8 on 2020-08-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0071_auto_20200820_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category_name',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category_name',
            field=models.ManyToManyField(to='website.Categories'),
        ),
    ]
