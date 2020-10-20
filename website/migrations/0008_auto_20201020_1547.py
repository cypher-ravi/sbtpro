# Generated by Django 3.1 on 2020-10-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20201020_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frenchisecontact',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='frenchisecontact',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='frenchisecontact',
            name='frenchise_option',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='frenchisecontact',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
