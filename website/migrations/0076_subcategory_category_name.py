# Generated by Django 3.0.8 on 2020-08-20 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0075_remove_subcategory_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='website.Categories'),
        ),
    ]