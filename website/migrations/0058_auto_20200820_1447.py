# Generated by Django 3.0.8 on 2020-08-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0057_auto_20200820_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='sub_category_name',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
