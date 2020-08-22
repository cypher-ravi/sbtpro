# Generated by Django 3.0.8 on 2020-08-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0078_auto_20200820_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('feed_back', models.BooleanField()),
                ('Comments', models.TextField()),
                ('customer_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]