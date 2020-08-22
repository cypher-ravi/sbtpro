# Generated by Django 3.0.8 on 2020-08-20 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0056_auto_20200820_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Categories'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category_name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]