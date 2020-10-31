from django.db import models
from website.models import Categories
from restapi.models import *
from dashboard.models import *
# from dashboard.models import Employee
from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()
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
    """
    Store vendor services
    """
    service_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,default='')
    description = models.TextField(max_length=200,default='')
    service_is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Vendor Services"

    def __str__(self):
        return self.title
    
class VendorVideos(models.Model):
    """
    Store vendor videos
    """
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,default='')
    video_url = models.URLField(default='')

    class Meta:
        verbose_name_plural = "Vendor videos"

    def __str__(self):
        return self.video_url



class VendorImages(models.Model):
    """
    Store vendor images
    """
    image_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,default='',blank=True,null=True)
    image_url = models.ImageField(upload_to="website/images/vendors/VendorImages", default="",blank=True,null=True)
    image = models.TextField(max_length=16383,blank=True, null=True, default='')

    class Meta:
        verbose_name_plural = "Vendor images"

    def __str__(self):
        return self.image

class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True, blank=True)
    vendor_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)
    Name = models.CharField(max_length=50, default='',null= True, blank=True)
    Company_Name = models.CharField(max_length=100, default='',null= True, blank=True)
    Busniess_Type = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True,blank=True)
    # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,blank=True,null=True)
    Service_decsription = models.TextField(max_length=1000, default='',null= True, blank=True)
    Mobile_No =models.CharField(max_length=14, default='',null= True, blank=True)
    Mobile_No_2 = models.CharField(max_length=14, default='',null= True, blank=True)
    Address1 = models.CharField(max_length=100, default='',null= True, blank=True)
    Address2 = models.CharField(max_length=100, blank=True, null=True, default='')
    city = models.CharField(max_length=100, default='',null= True, blank=True)
    state = models.CharField(max_length=100, choices=VALID_STATE_CHOICES, default='Please Select',null= True, blank=True)
    PinCode = models.CharField(max_length=100,null= True, blank=True)
    Contact_Person = models.CharField(max_length=100, default='', blank=True, null=True)
    EmailID = models.CharField(max_length=50,null=True, blank=True)
    Landline = models.CharField(max_length=50,null=True, blank=True)
    GST_No = models.CharField(max_length=15,null=True, blank=True)
    Pan_No = models.CharField(max_length=11,null=True, blank=True)
    TIN_No = models.CharField(max_length=11,null=True, blank=True)
    Registered_Trade_Name = models.CharField(max_length=100, blank=True, null=True, default='')
    Facebook_URL = models.CharField(max_length=200, blank=True, null=True)
    Twitter_URL = models.CharField(max_length=200, blank=True, null=True)
    website_URL = models.CharField(max_length=200, blank=True, null=True)
    instagram_URL = models.CharField(max_length=200, blank=True, null=True)
    youtube_URL = models.CharField(max_length=200, blank=True, null=True)
    established_date = models.CharField(max_length=200, blank=True, null=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New',null= True, blank=True)
    Other_Info = models.CharField(max_length=200, blank=True, null=True)
    Discount_Percentage = models.CharField(max_length=100, null= True, blank=True)
    Longitude = models.CharField(max_length=100, null=True, blank=True)
    Latitude = models.CharField(max_length=100, null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(upload_to="website/images/vendors", default="",null=True,blank=True)
    vendor_services = models.ManyToManyField(VendorServices,blank=True)
    vendor_video = models.ForeignKey(VendorVideos,on_delete=models.CASCADE,null=True,blank=True)
    vendor_images = models.ManyToManyField(VendorImages,blank=True)
    TYPE_OF_BUSINESS =  (
    ("none", "Please Select"),
    ("retailer", "retailer"),
    ("publication", "publication"),
    ("manufacture", "manufacture"),
    ("professional service", "professional service"),
    ("consultant", "consultant"),
    ("distribution", "distribution"),
    ("service provider", "service provider"),
    ("freght/transportation", "freght/transportation"),
    ("authorised agent", "authorised agent"),
    ("trader", "trader"),
    ("other", "other"),
    )
    type_of_commodity_or_business = models.CharField(max_length=100, choices=TYPE_OF_BUSINESS, default='service provider',null= True, blank=True)

    SERVICE_AREA =  (
    ("none", "Please Select"),
    ("village", "village"),
    ("district", "vistrict"),
    ("tehsil", "tehsil"),
    ("state", "state"),
    )
    geograpgical_area = models.CharField(max_length=20, choices=SERVICE_AREA, default='none',null= True, blank=True)
    BUSINESS_HISTORY =  (
    ("none", "Please Select"),
    ("YES", "YES"),
    ("NO", "NO"),
    )
    LEGAL_STRUCTURE = (
        ("none", "Please Select"),
        ("partnership", "partnership"),
        ("soleproprietship", "soleproprietship"),
        ("franchise", "franchise"),
        ("joint venture", "joint venture"),
        ("non-profit", "non-profit"),
    )
    legal_structure =  models.CharField(max_length=20, choices=LEGAL_STRUCTURE, default='none',null= True, blank=True)
    business_history_with_sbt = models.CharField(max_length=20, choices=BUSINESS_HISTORY, default='none',null= True, blank=True)
    
    registration_fee = models.ForeignKey(Plan,on_delete=models.CASCADE,null=True,blank=True)
    vendor_is_active = models.BooleanField(default=False,blank=True,null=True)
   
    # employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    class Meta:
        ordering = ['vendor_id']

    def __str__(self):
        return self.Company_Name


