# Generated by Django 3.0.8 on 2020-08-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0080_auto_20200822_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(),
        ),
    ]
