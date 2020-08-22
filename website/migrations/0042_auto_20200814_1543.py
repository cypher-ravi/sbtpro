# Generated by Django 3.0.8 on 2020-08-14 15:43

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0041_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name10',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name2',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name3',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name4',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name5',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name6',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name7',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name8',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='sub_category_name9',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=50)),
                ('Mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Mobile_No_2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Address1', models.CharField(default='', max_length=100)),
                ('Address2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(choices=[('1', 'Andaman and Nicobar Islands'), ('2', 'Andra Pradesh'), ('3', 'Arunachal Pradesh'), ('4', 'Assam'), ('5', 'Bihar'), ('6', 'Chhattisgarh'), ('7', 'Chandigarh'), ('8', 'Dadar and Nagar Haveli'), ('9', 'Daman and Diu'), ('10', 'Delhi'), ('11', 'Goa'), ('12', 'Gujarat'), ('13', 'Haryana'), ('14', 'Himachal Pradesh'), ('15', 'Jammu and Kashmir'), ('16', 'Jharkhand'), ('17', 'Karnataka'), ('18', 'Kerala'), ('19', 'Lakshadeep'), ('20', 'Madya Pradesh'), ('21', 'Maharashtra'), ('22', 'Manipur'), ('23', 'Meghalaya'), ('24', 'Mizoram'), ('25', 'Nagaland'), ('26', 'Orissa'), ('27', 'Punjab'), ('28', 'Pondicherry'), ('29', 'Rajasthan'), ('30', 'Sikkim'), ('31', 'Tamil Nadu'), ('32', 'Telagana'), ('33', 'Tripura'), ('34', 'Uttaranchal'), ('35', 'Uttar Pradesh'), ('36', 'West Bengal')], default='Please Select', max_length=100)),
                ('Contact_Person', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('EmailID', models.EmailField(blank=True, max_length=254, null=True)),
                ('Landline', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('GST_No', models.IntegerField(null=True)),
                ('Pan_No', models.IntegerField(null=True)),
                ('TIN_No', models.IntegerField(null=True)),
                ('Registered_Trade_Name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('Facebook_URL', models.URLField(blank=True, null=True)),
                ('Twitter_URL', models.URLField(blank=True, null=True)),
                ('website_URL', models.URLField(blank=True, null=True)),
                ('Status', models.CharField(choices=[('1', 'Please Select'), ('2', 'New'), ('3', 'Verified')], default='New', max_length=20)),
                ('Other_Info', models.CharField(blank=True, max_length=200, null=True)),
                ('Discount_Percentage', models.IntegerField(null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('Image', models.ImageField(default='', upload_to='website/images/vendors')),
                ('Busniess_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Categories')),
            ],
        ),
    ]