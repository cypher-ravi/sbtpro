# Generated by Django 3.1 on 2020-11-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20201031_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_type',
            field=models.CharField(blank=True, choices=[('root', 'root'), ('state', 'state'), ('district', 'district'), ('tehsil', 'tehsil'), ('village', 'village')], max_length=100, null=True),
        ),
    ]
