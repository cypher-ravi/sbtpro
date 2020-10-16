from django.db import models
from website.models import Categories
from restapi.models import *
# from dashboard.models import Employee
from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your models here.

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
    ("Please Select", "Please Select"),
    ("Andra Pradesh", "Andra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Chandigarh", "Chandigarh"),
    ("Dadar and Nagar Haveli", "Dadar and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Delhi", "Delhi"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Lakshadeep", "Lakshadeep"),
    ("Madya Pradesh", "Madya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Orissa", "Orissa"),
    ("Punjab", "Punjab"),
    ("Pondicherry", "Pondicherry"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telagana", "Telagana"),
    ("Tripura", "Tripura"),
    ("Uttaranchal", "Uttaranchal"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Island", "Andaman and Nicobar Island"),

)

class VendorServices(models.Model):
    service_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,default='')
    description = models.TextField(max_length=200,default='')
    service_is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Vendor Services"

    def __str__(self):
        return self.title
    
class VendorVideos(models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,default='')
    video_url = models.URLField(default='')

    class Meta:
        verbose_name_plural = "Vendor videos"

    def __str__(self):
        return self.video_url

class VendorImages(models.Model):
    image_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,default='')
    image_url = models.URLField(default='')

    class Meta:
        verbose_name_plural = "Vendor images"

    def __str__(self):
        return self.image_url



class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, default='')
    Company_Name = models.CharField(max_length=100, default='')
    Busniess_Type = models.ForeignKey(Categories, on_delete=models.CASCADE)
    # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,blank=True,null=True)
    Service_decsription = models.TextField(max_length=1000, default='')
    Mobile_No = PhoneNumberField()
    Mobile_No_2 = PhoneNumberField()
    Address1 = models.CharField(max_length=100, default='')
    Address2 = models.CharField(max_length=100, blank=True, null=True, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, choices=VALID_STATE_CHOICES, default='Please Select')
    PinCode = models.IntegerField()
    Contact_Person = models.CharField(max_length=100, default='', blank=True, null=True)
    EmailID = models.EmailField(null=True, blank=True)
    Landline = PhoneNumberField(null=True)
    GST_No = models.IntegerField(null=True, blank=True)
    Pan_No = models.IntegerField(null=True, blank=True)
    TIN_No = models.IntegerField(null=True, blank=True)
    Registered_Trade_Name = models.CharField(max_length=100, blank=True, null=True, default='')
    Facebook_URL = models.URLField(max_length=200, blank=True, null=True)
    Twitter_URL = models.URLField(max_length=200, blank=True, null=True)
    website_URL = models.URLField(max_length=200, blank=True, null=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    Other_Info = models.CharField(max_length=200, blank=True, null=True)
    Discount_Percentage = models.IntegerField(null=True)
    Longitude = models.FloatField(null=True, blank=True)
    Latitude = models.FloatField(null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(upload_to="website/images/vendors", default="")
    vendor_services = models.ManyToManyField(VendorServices)
    vendor_video = models.ForeignKey(VendorVideos,on_delete=models.CASCADE,null=True,blank=True)
    vendor_images = models.ManyToManyField(VendorImages,blank=True)
    TYPE_OF_BUSINESS =  (
    ("none", "Please Select"),
    ("consultant", "Consultant"),
    ("distrubution", "Distrubution"),
    ("service provider", "Service Provider"),
    ("freght/transportation", "Freght/Transportation"),
    ("authorised agent", "Authorised Agent"),
    ("trader", "Trader"),
    ("trader", "Other"),
    )
    type_of_commodity_or_business = models.CharField(max_length=100, choices=TYPE_OF_BUSINESS, default='service provider')

    SERVICE_AREA =  (
    ("none", "Please Select"),
    ("village", "Village"),
    ("district", "District"),
    ("tehsil", "Tehsil"),
    ("state", "State"),
    )
    geograpgical_area = models.CharField(max_length=20, choices=SERVICE_AREA, default='none')
    BUSINESS_HISTORY =  (
    ("none", "Please Select"),
    ("YES", "YES"),
    ("NO", "NO"),
    )
    business_history_with_sbt = models.CharField(max_length=20, choices=BUSINESS_HISTORY, default='none')
    REGISTRATION_FEE =  (
    ("none", "Please Select"),
    ("INR 1200/per month", "INR 1200/per month"),
    ("INR 12000/per yearly", "INR 12000/per yearly"),
    ("Registration Fee(INR 100@ lifetime)", "Registration Fee(INR 100@ lifetime)"),
    ("Sbt marketing concept", "Sbt marketing concept"),
    )
    registration_fee = models.CharField(max_length=100, choices=REGISTRATION_FEE, default='none')
    # employee = models.ForeignKey(Employee,on_delete=models.CASCADE)


    def __str__(self):
        return self.Name


