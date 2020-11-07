# Generated by Django 3.1 on 2020-11-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_auto_20201107_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Address1',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Address2',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='father_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
