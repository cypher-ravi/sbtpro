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

class DailyAttendance(models.Model):
    ATTENDACE_CHOICES = (
    ("is_present", "present"),
    ("is_absent", "absent"),

    )
    attendance = models.CharField(max_length=20,choices=ATTENDACE_CHOICES,default='absent')
    punch_time = models.DateTimeField()
    punch_out_time = models.DateTimeField(null=True,blank=True)
    vendor = models.CharField(max_length=50,null=True,blank=True)
    work_description = models.TextField(max_length=1000,null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.attendance) + ' today punch time is ' + str(self.punch_time)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=20,default='')
    father_name = models.CharField(max_length=20,default='')
    Mobile_No = PhoneNumberField()
    Mobile_No_2 = PhoneNumberField()
    Address1 = models.CharField(max_length=100, default='')
    Address2 = models.CharField(max_length=100, blank=True, null=True, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, choices=VALID_STATE_CHOICES, default='Please Select')
    zipcode = models.IntegerField()
    country = CountryField()
    EmailID = models.EmailField(null=True, blank=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    gross_salary = models.BigIntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='Please Select')
    date_of_birth = models.DateField()
    extra_Info = models.TextField(max_length=200, blank=True, null=True)
    Contact_Person = models.CharField(max_length=100, default='', blank=True, null=True)
    employee_is_active = models.BooleanField(default=False)
    employee_designation = models.CharField(max_length=30,default='')
    Image = models.ImageField(upload_to="dashboard/images/Employee", blank=True,null=True)
    daily_attendance = models.ForeignKey(DailyAttendance,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.employee_name


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
    

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=20,default='')
    Mobile_No = PhoneNumberField()
    Mobile_No_2 = PhoneNumberField(blank=True,null=True)
    Address1 = models.CharField(max_length=100, default='')
    Address2 = models.CharField(max_length=100, blank=True, null=True, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, choices=VALID_STATE_CHOICES, default='Please Select')
    zipcode = models.IntegerField()
    country = CountryField()
    EmailID = models.EmailField(null=True, blank=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='Please Select')
    extra_Info = models.TextField(max_length=200, blank=True, null=True)
    Contact_Person = models.CharField(max_length=100, default='', blank=True, null=True)
    customer_is_active = models.BooleanField(default=False)
    subscription_plan_taken = models.ForeignKey('website.Plan',on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name


