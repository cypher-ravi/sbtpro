# Generated by Django 3.0.8 on 2020-08-14 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_auto_20200814_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_id',
        ),
        migrations.AddField(
            model_name='service',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
