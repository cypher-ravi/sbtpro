# Generated by Django 3.1 on 2020-09-12 06:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200910_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_resume',
            name='Resume',
            field=models.FileField(blank=True, null=True, upload_to='website/resumes', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'word'])]),
        ),
    ]