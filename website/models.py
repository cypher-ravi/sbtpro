from restapi.models import *
# from dashboard.models import Employee
from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField
"""from django.contrib.auth.models import User
"""
from django.utils import timezone
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
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


"""class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Fathers_name = models.CharField(max_length=50, blank=True)
    Mobile_No = PhoneNumberField()
    Mobile_No_2 = PhoneNumberField()
    Address = models.CharField(max_length=100, default='')
    City = models.CharField(max_length=100, default='')
    State = models.CharField(max_length=100, choices=VALID_STATE_CHOICES, default='Please Select')
    PinCode = models.IntegerField()
    Gross_Salary = models.IntegerField()
    Gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='Please Select')
    Date_of_Birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
"""

# Create your models here.
# model for listing form
class FreeListing(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    Company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    mobile = models.BigIntegerField()
    submit_date = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name_plural = "Vendor Requests"

    def __str__(self):
        return self.Company_name

    


class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=25, null=False)
    plan_amount = models.IntegerField(null=False)
    minimum_discount = models.IntegerField(null = False)
    maximum_discount = models.IntegerField(null = False)
    description_1 = models.CharField(max_length=50, null=True)
    description_2 = models.CharField(max_length=50, null=True)
    description_3 = models.CharField(max_length=50, null=True)
    description_4 = models.CharField(max_length=50, null=True)
    plan_img = models.ImageField(upload_to="website/membershipcard", default="")
    
    def __str__(self):
        return self.plan_name


"""class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.IntegerField(null=False)
    email_id = models.CharField(max_length=45)
    name = models.CharField(max_length=20)
    phone = PhoneNumberField()
    address = models.CharField(max_length=111)
    state = models.CharField(max_length=111, choices=VALID_STATE_CHOICES)
    city = models.CharField(max_length=111)
    order_date =  models.DateTimeField(auto_now_add=True)
    zip_code = models.CharField(max_length=8)
    amount = models.IntegerField(null=False)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order_completed = models.BooleanField()

    def __str__(self):
        return self.email_id"""


"""class Order_Payment(models.Model):
    id = models.AutoField(primary_key = True)
    order_summary = models.ForeignKey(Order, on_delete = models.CASCADE)
    # paytm responses 
    currency = models.CharField(max_length=8) # INR
    gateway_name = models.CharField(max_length=25) # WALLET
    response_message = models.TextField() # Txn Success
    bank_name = models.CharField(max_length=25) # WALLET
    Payment_mode = models.CharField(max_length=25)# PPI
    # MID = models.CharField(max_length=8) # VdMxPH61970223458566
    response_code = models.CharField(max_length=3) # 01
    txn_id = models.TextField() #  20200905111212800110168406201874634
    txn_amount = models.CharField(max_length=9) #  2400.00
    order_id = models.IntegerField() #  6556
    status = models.CharField(max_length=12) # TXN_SUCCESS
    bank_txn_id = models.CharField(max_length=12) #  63209779
    txn_date = models.CharField(max_length=23) #  2020-09-05 18:51:59.0
    refund_amount = models.IntegerField(default=0.00) #  0.00
    # test = models.CharField(max_length=23)
    
    def __str__(self):
        return str(self.order_summary)
"""


class Job(models.Model):
    seeker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    submit_date =  models.DateTimeField(auto_now_add=True)
    # email = models.EmailField(max_length=50, default='',)
    education = models.CharField(max_length=200, default='')
    experience = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class Upload_resume(models.Model):
    resume_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='', blank=True, null=True)
    # copy_resume = models.CharField(max_length=5000, default='',blank=True,null=True)

    filling_date =  models.DateTimeField(auto_now_add=True)
    Resume = models.FileField(blank=True, null=True,upload_to='website/JobResumes',
                              validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'word'])])

    def __str__(self):
        return self.name


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, default='')
    Image = models.FileField(blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
    category_description = models.TextField(max_length=100,default='')
    category_is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['category_id']

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=50, null=False, default='')
    category_name = models.ForeignKey(to=Categories, related_name='sub_category', null=True, blank=True,
                                      on_delete=models.CASCADE)
    

    def __str__(self):
        return self.sub_category_name


class Sub_sub_category(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    sub_sub_category_name = models.CharField(max_length=50, null=False, default='')
    sub_category_name = models.ForeignKey(to=Subcategory, related_name='sub_category', null=True, blank=True,
                                          on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_sub_category_name


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=50)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=150, default="")
    subcategory = models.ForeignKey(to=Subcategory, null=True, blank=True,
                                          on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    service_desc = models.TextField(max_length=200, default='')
    publish_date = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(upload_to="website/images", default="")

    def __str__(self):
        return self.service_name


class TOP(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50, default='')
    Busniess_Type = models.ForeignKey(Categories, on_delete=models.CASCADE)
    vendor_work_desc = models.TextField(max_length=1000, default='')
    address = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    vendor_mobile_no = PhoneNumberField()
    vendor_email = models.EmailField(null=True, blank=True)
    Image = models.ImageField(upload_to="website/images/TOPvendors", default="")
    APP_CHOICES = (
    ("True", "True"),
    ("False", "False"),
    )


    app_exists = models.CharField(choices=APP_CHOICES,max_length=20,default=False)
    app_url = models.CharField(max_length=50,default=False)


    def __str__(self):
        return self.vendor_name


class ServiceContact(models.Model):
    registrant_id = models.AutoField(primary_key=True)
    registrant_id = models.AutoField(primary_key=True)
    registrant_name = models.CharField(max_length=50, default='')
    registrant_mobile_no = PhoneNumberField()
    submit_date =  models.DateTimeField(auto_now_add=True)
    registrant_interest = models.CharField(max_length=50, default='')
    registrant_query = models.TextField()

    def __str__(self):
        return self.registrant_name





# for sbt trading form
class Trading(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    address_from = models.CharField(max_length=50)
    address_to = models.CharField(max_length=50)
    submit_date = models.DateTimeField(auto_now_add=True)
    zip_code = models.IntegerField(default='')
    mobile = PhoneNumberField()

    def __str__(self):
        return self.customer_name


class Faq(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_category = models.CharField(max_length=100, default='')
    market_executive_name = models.CharField(max_length=50, default='')
    submit_date = models.DateTimeField(auto_now_add=True)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question_category


class QueryContact(models.Model):
    query_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    mobile = PhoneNumberField()
    submit_date =  models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.customer_name


class Feedback(models.Model):
    customer_id = models.AutoField(primary_key=True)
    feed_back = models.CharField(max_length=50, default=False)
    submit_date =  models.DateTimeField(auto_now_add=True)
    Comments = models.TextField()
    customer_name = models.CharField(max_length=50, default='')
    email = models.EmailField()

    def __str__(self):
        return self.customer_name


class Contactviacategory(models.Model):
    registrant_id = models.AutoField(primary_key=True)
    registrant_name = models.CharField(max_length=50, default='')
    registrant_mobile_no = PhoneNumberField()
    calling_time = models.CharField(max_length=50, default='')
    submit_date =  models.DateTimeField(auto_now_add=True)
    service_name = models.ForeignKey(to=Subcategory, on_delete=models.CASCADE, default='', blank=True, null=True)
    sub_service_name = models.ForeignKey(to=Sub_sub_category, on_delete=models.CASCADE, default='', blank=True,
                                         null=True)

    def __str__(self):
        return self.registrant_name


class FrenchiseContact(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    mobile_no = models.CharField(max_length=14,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=200, default='')
    frenchise_option = models.CharField(max_length=50, default='',blank=True,null=True)
    company_name = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(max_length=1000,blank=True,null=True)
    submit_time =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Frenchise Requests'

    def __str__(self):
        return self.name


class AddTestimonial(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50, default='')
    quote = models.TextField(max_length=350, default='')
    submit_date =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.customer_name


class Pricing(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 27)
	description = models.TextField()

	def __str__(self):
		return self.name