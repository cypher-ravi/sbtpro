# Generated by Django 3.1 on 2020-10-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0008_auto_20201022_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Image',
            field=models.ImageField(default='', upload_to='website/images/vendors'),
        ),
    ]