# Generated by Django 3.1 on 2020-11-06 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False)),
                ('banner_name', models.CharField(default='', max_length=50)),
                ('banner_img', models.ImageField(upload_to='dashboard/images/banner_1')),
            ],
        ),
        migrations.CreateModel(
            name='Banner2',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False)),
                ('banner_name', models.CharField(default='', max_length=50)),
                ('banner_img', models.ImageField(upload_to='dashboard/images/banner_2')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_type', models.CharField(blank=True, choices=[('root', 'root'), ('state', 'state'), ('district', 'district'), ('tehsil', 'tehsil'), ('village', 'village')], max_length=100, null=True)),
                ('branch_name', models.CharField(default='', max_length=20)),
                ('Mobile_No', models.CharField(blank=True, max_length=20, null=True)),
                ('Mobile_No_2', models.CharField(blank=True, max_length=20, null=True)),
                ('Address1', models.CharField(default='', max_length=100)),
                ('Address2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(choices=[('1', 'Please Select'), ('2', 'Andra Pradesh'), ('3', 'Arunachal Pradesh'), ('4', 'Assam'), ('5', 'Bihar'), ('6', 'Chhattisgarh'), ('7', 'Chandigarh'), ('8', 'Dadar and Nagar Haveli'), ('9', 'Daman and Diu'), ('10', 'Delhi'), ('11', 'Goa'), ('12', 'Gujarat'), ('13', 'Haryana'), ('14', 'Himachal Pradesh'), ('15', 'Jammu and Kashmir'), ('16', 'Jharkhand'), ('17', 'Karnataka'), ('18', 'Kerala'), ('19', 'Lakshadeep'), ('20', 'Madya Pradesh'), ('21', 'Maharashtra'), ('22', 'Manipur'), ('23', 'Meghalaya'), ('24', 'Mizoram'), ('25', 'Nagaland'), ('26', 'Orissa'), ('27', 'Punjab'), ('28', 'Pondicherry'), ('29', 'Rajasthan'), ('30', 'Sikkim'), ('31', 'Tamil Nadu'), ('32', 'Telagana'), ('33', 'Tripura'), ('34', 'Uttaranchal'), ('35', 'Uttar Pradesh'), ('36', 'West Bengal'), ('37', 'Andaman and Nicobar Island')], default='Please Select', max_length=100)),
                ('zipcode', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('EmailID', models.EmailField(blank=True, max_length=254, null=True)),
                ('regsitration_date', models.DateTimeField(auto_now_add=True)),
                ('landline_no', models.CharField(blank=True, max_length=15, null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('extra_Info', models.TextField(blank=True, max_length=200, null=True)),
                ('Contact_Person', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('branch_is_active', models.BooleanField(default=False)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='dashboard/images/branch')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BranchReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('report_detail', models.TextField(max_length=5000)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.branch')),
            ],
        ),
        migrations.CreateModel(
            name='BranchContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=5000)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.branch')),
            ],
        ),
    ]
