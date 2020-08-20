# Generated by Django 3.0.8 on 2020-08-20 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0055_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
