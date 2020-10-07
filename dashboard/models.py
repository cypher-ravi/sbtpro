from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from website.models import VALID_STATE_CHOICES,GENDER_CHOICES
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


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