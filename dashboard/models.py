from website.models import *

from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ("1", "Please Select"),
    ("2", "Male"),
    ("3", "Female"),
    ("4", "Other"),

)

STATUS_CHOICES = (
    ("1", "Please Select"),
    ("2", "New"),
    ("3", "Verified"),

)

VALID_STATE_CHOICES = (
    ("1", "Please Select"),
    ("2", "Andra Pradesh"),
    ("3", "Arunachal Pradesh"),
    ("4", "Assam"),
    ("5", "Bihar"),
    ("6", "Chhattisgarh"),
    ("7", "Chandigarh"),
    ("8", "Dadar and Nagar Haveli"),
    ("9", "Daman and Diu"),
    ("10", "Delhi"),
    ("11", "Goa"),
    ("12", "Gujarat"),
    ("13", "Haryana"),
    ("14", "Himachal Pradesh"),
    ("15", "Jammu and Kashmir"),
    ("16", "Jharkhand"),
    ("17", "Karnataka"),
    ("18", "Kerala"),
    ("19", "Lakshadeep"),
    ("20", "Madya Pradesh"),
    ("21", "Maharashtra"),
    ("22", "Manipur"),
    ("23", "Meghalaya"),
    ("24", "Mizoram"),
    ("25", "Nagaland"),
    ("26", "Orissa"),
    ("27", "Punjab"),
    ("28", "Pondicherry"),
    ("29", "Rajasthan"),
    ("30", "Sikkim"),
    ("31", "Tamil Nadu"),
    ("32", "Telagana"),
    ("33", "Tripura"),
    ("34", "Uttaranchal"),
    ("35", "Uttar Pradesh"),
    ("36", "West Bengal"),
    ("37", "Andaman and Nicobar Island"),

)

class UserType(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    is_branch_user = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


# Create your models here.
class Branch(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    branch_user_type = models.OneToOneField(UserType,related_name='branch_user',on_delete=models.CASCADE,blank=True,null=True)
    branch_name = models.CharField(max_length=20,default='')
    Mobile_No = PhoneNumberField()
    Mobile_No_2 = PhoneNumberField()
    Address1 = models.CharField(max_length=100, default='')
    Address2 = models.CharField(max_length=100, blank=True, null=True, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, choices=VALID_STATE_CHOICES, default='Please Select')
    zipcode = models.IntegerField()
    country = CountryField()
    EmailID = models.EmailField(null=True, blank=True)
    regsitration_date = models.DateTimeField(auto_now_add=True)
    landline_no = PhoneNumberField()
    Longitude = models.FloatField(null=True, blank=True)
    Latitude = models.FloatField(null=True, blank=True)
    extra_Info = models.TextField(max_length=200, blank=True, null=True)
    Contact_Person = models.CharField(max_length=100, default='', blank=True, null=True)
    branch_is_active = models.BooleanField(default=False)
    Image = models.ImageField(upload_to="dashboard/images/branch", blank=True,null=True)
    

    def __str__(self):
        return self.branch_name




class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    banner_name = models.CharField(max_length=50,default='')
    banner_img = models.ImageField(upload_to="dashboard/images/banner_1")

    def __str__(self):
        return self.banner_name


class Banner2(models.Model):
    banner_id = models.AutoField(primary_key=True)
    banner_name = models.CharField(max_length=50,default='')
    banner_img = models.ImageField(upload_to="dashboard/images/banner_2")

    def __str__(self):
        return self.banner_name
    

