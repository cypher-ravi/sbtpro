# Generated by Django 3.1 on 2020-10-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorVideos',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20)),
                ('video_url', models.URLField(default='')),
            ],
            options={
                'verbose_name_plural': 'Vendor videos',
            },
        ),
    ]
