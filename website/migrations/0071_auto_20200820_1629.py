# Generated by Django 3.0.8 on 2020-08-20 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0070_auto_20200820_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.Categories'),
        ),
        migrations.AlterField(
            model_name='trendingservices',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.Categories'),
        ),
        migrations.AlterField(
            model_name='trendingservices',
            name='subcategory',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.Subcategory'),
        ),
    ]