# Generated by Django 3.1 on 2020-10-16 05:13

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(choices=[('is_present', 'present'), ('is_absent', 'absent')], default='absent', max_length=20)),
                ('punch_time', models.DateTimeField()),
                ('punch_out_time', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.CharField(blank=True, max_length=50, null=True)),
                ('work_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(default='', max_length=20)),
                ('father_name', models.CharField(default='', max_length=20)),
                ('Mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Mobile_No_2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Address1', models.CharField(default='', max_length=100)),
                ('Address2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(choices=[('Please Select', 'Please Select'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Chandigarh', 'Chandigarh'), ('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadeep', 'Lakshadeep'), ('Madya Pradesh', 'Madya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Pondicherry', 'Pondicherry'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telagana', 'Telagana'), ('Tripura', 'Tripura'), ('Uttaranchal', 'Uttaranchal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Island', 'Andaman and Nicobar Island')], default='Please Select', max_length=100)),
                ('zipcode', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('EmailID', models.EmailField(blank=True, max_length=254, null=True)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('gross_salary', models.BigIntegerField()),
                ('gender', models.CharField(choices=[('1', 'Please Select'), ('2', 'Male'), ('3', 'Female'), ('4', 'Other')], default='Please Select', max_length=100)),
                ('date_of_birth', models.DateField()),
                ('extra_Info', models.TextField(blank=True, max_length=200, null=True)),
                ('Contact_Person', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('employee_is_active', models.BooleanField(default=False)),
                ('employee_designation', models.CharField(default='', max_length=30)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Employee')),
                ('daily_attendance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.dailyattendance')),
            ],
        ),
    ]
