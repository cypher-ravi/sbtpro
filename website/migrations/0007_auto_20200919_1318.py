# Generated by Django 3.1 on 2020-09-19 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200919_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('1', 'Please Select'), ('2', 'Andra Pradesh'), ('3', 'Arunachal Pradesh'), ('4', 'Assam'), ('5', 'Bihar'), ('6', 'Chhattisgarh'), ('7', 'Chandigarh'), ('8', 'Dadar and Nagar Haveli'), ('9', 'Daman and Diu'), ('10', 'Delhi'), ('11', 'Goa'), ('12', 'Gujarat'), ('13', 'Haryana'), ('14', 'Himachal Pradesh'), ('15', 'Jammu and Kashmir'), ('16', 'Jharkhand'), ('17', 'Karnataka'), ('18', 'Kerala'), ('19', 'Lakshadeep'), ('20', 'Madya Pradesh'), ('21', 'Maharashtra'), ('22', 'Manipur'), ('23', 'Meghalaya'), ('24', 'Mizoram'), ('25', 'Nagaland'), ('26', 'Orissa'), ('27', 'Punjab'), ('28', 'Pondicherry'), ('29', 'Rajasthan'), ('30', 'Sikkim'), ('31', 'Tamil Nadu'), ('32', 'Telagana'), ('33', 'Tripura'), ('34', 'Uttaranchal'), ('35', 'Uttar Pradesh'), ('36', 'West Bengal'), ('37', 'Andaman and Nicobar Island')], max_length=111),
        ),
    ]
