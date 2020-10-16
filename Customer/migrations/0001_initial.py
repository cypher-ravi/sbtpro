# Generated by Django 3.1 on 2020-10-16 05:15

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0014_auto_20201016_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='', max_length=20)),
                ('Mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Mobile_No_2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('Address1', models.CharField(default='', max_length=100)),
                ('Address2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(choices=[('Please Select', 'Please Select'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Chandigarh', 'Chandigarh'), ('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadeep', 'Lakshadeep'), ('Madya Pradesh', 'Madya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Pondicherry', 'Pondicherry'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telagana', 'Telagana'), ('Tripura', 'Tripura'), ('Uttaranchal', 'Uttaranchal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Island', 'Andaman and Nicobar Island')], default='Please Select', max_length=100)),
                ('zipcode', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('EmailID', models.EmailField(blank=True, max_length=254, null=True)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('1', 'Please Select'), ('2', 'Male'), ('3', 'Female'), ('4', 'Other')], default='Please Select', max_length=100)),
                ('extra_Info', models.TextField(blank=True, max_length=200, null=True)),
                ('Contact_Person', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('customer_is_active', models.BooleanField(default=False)),
                ('subscription_plan_taken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.plan')),
            ],
        ),
    ]