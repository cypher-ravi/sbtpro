# Generated by Django 3.0.8 on 2020-08-20 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0074_subcategory_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category_name',
        ),
    ]
