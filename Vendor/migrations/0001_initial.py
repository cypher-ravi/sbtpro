# Generated by Django 3.1 on 2020-10-17 08:00

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorImages',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20)),
                ('image_url', models.ImageField(default='', upload_to='website/images/vendors/VendorImages')),
            ],
            options={
                'verbose_name_plural': 'Vendor images',
            },
        ),
        migrations.CreateModel(
            name='VendorServices',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20)),
                ('description', models.TextField(default='', max_length=200)),
                ('service_is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Vendor Services',
            },
        ),
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
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=50)),
                ('Company_Name', models.CharField(default='', max_length=100)),
                ('Service_decsription', models.TextField(default='', max_length=1000)),
                ('Mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Mobile_No_2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Address1', models.CharField(default='', max_length=100)),
                ('Address2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(choices=[('Please Select', 'Please Select'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Chandigarh', 'Chandigarh'), ('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadeep', 'Lakshadeep'), ('Madya Pradesh', 'Madya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Pondicherry', 'Pondicherry'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telagana', 'Telagana'), ('Tripura', 'Tripura'), ('Uttaranchal', 'Uttaranchal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Island', 'Andaman and Nicobar Island')], default='Please Select', max_length=100)),
                ('PinCode', models.IntegerField()),
                ('Contact_Person', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('EmailID', models.EmailField(blank=True, max_length=254, null=True)),
                ('Landline', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('GST_No', models.IntegerField(blank=True, null=True)),
                ('Pan_No', models.IntegerField(blank=True, null=True)),
                ('TIN_No', models.IntegerField(blank=True, null=True)),
                ('Registered_Trade_Name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('Facebook_URL', models.URLField(blank=True, null=True)),
                ('Twitter_URL', models.URLField(blank=True, null=True)),
                ('website_URL', models.URLField(blank=True, null=True)),
                ('Status', models.CharField(choices=[('1', 'Please Select'), ('2', 'New'), ('3', 'Verified')], default='New', max_length=20)),
                ('Other_Info', models.CharField(blank=True, max_length=200, null=True)),
                ('Discount_Percentage', models.IntegerField(null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('Image', models.ImageField(default='', upload_to='website/images/vendors')),
                ('type_of_commodity_or_business', models.CharField(choices=[('none', 'Please Select'), ('consultant', 'Consultant'), ('distrubution', 'Distrubution'), ('service provider', 'Service Provider'), ('freght/transportation', 'Freght/Transportation'), ('authorised agent', 'Authorised Agent'), ('trader', 'Trader'), ('trader', 'Other')], default='service provider', max_length=100)),
                ('geograpgical_area', models.CharField(choices=[('none', 'Please Select'), ('village', 'Village'), ('district', 'District'), ('tehsil', 'Tehsil'), ('state', 'State')], default='none', max_length=20)),
                ('business_history_with_sbt', models.CharField(choices=[('none', 'Please Select'), ('YES', 'YES'), ('NO', 'NO')], default='none', max_length=20)),
                ('registration_fee', models.CharField(choices=[('none', 'Please Select'), ('INR 1200/per month', 'INR 1200/per month'), ('INR 12000/per yearly', 'INR 12000/per yearly'), ('Registration Fee(INR 365@ lifetime)', 'Registration Fee(INR 100@ lifetime)'), ('Sbt marketing concept', 'Sbt marketing concept')], default='none', max_length=100)),
                ('Busniess_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.categories')),
            ],
        ),
    ]
