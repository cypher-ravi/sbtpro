# Generated by Django 3.1 on 2020-10-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20201014_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('Please Select', 'Please Select'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Chandigarh', 'Chandigarh'), ('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadeep', 'Lakshadeep'), ('Madya Pradesh', 'Madya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Pondicherry', 'Pondicherry'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telagana', 'Telagana'), ('Tripura', 'Tripura'), ('Uttaranchal', 'Uttaranchal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Island', 'Andaman and Nicobar Island')], max_length=111),
        ),
        migrations.AlterField(
            model_name='profile',
            name='State',
            field=models.CharField(choices=[('Please Select', 'Please Select'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Chandigarh', 'Chandigarh'), ('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadeep', 'Lakshadeep'), ('Madya Pradesh', 'Madya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Pondicherry', 'Pondicherry'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telagana', 'Telagana'), ('Tripura', 'Tripura'), ('Uttaranchal', 'Uttaranchal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Island', 'Andaman and Nicobar Island')], default='Please Select', max_length=100),
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]