from django.db import models
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField


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
    zip_code = models.IntegerField(default='')
    mobile = models.IntegerField(default='')
    email = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.Company_name


class Plans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=25, null=False)
    plan_amount = models.IntegerField(null=False)
    description_1 = models.CharField(max_length=50, null=True)
    description_2 = models.CharField(max_length=50, null=True)
    description_3 = models.CharField(max_length=50, null=True)
    description_4 = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.plan_name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(null=False)
    email_id = models.CharField(max_length=45)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=8)
    payment_status = models.CharField(max_length=8)
    amount = models.IntegerField(null=False)
    plan_id = models.ForeignKey(Plans, on_delete=models.CASCADE)
    # amount_status = models.CharField(max_length=25)
    # response_code = models.IntegerField()
    # response_msg = models.CharField(max_length=111)

    def __str__(self):
        return self.email_id





class Job(models.Model):
    seeker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(default='')
    # email = models.EmailField(max_length=50, default='',)
    education = models.CharField(max_length=200, default='')
    experience = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class Upload_resume(models.Model):
    resume_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='',blank=True,null=True)
    # copy_resume = models.CharField(max_length=5000, default='',blank=True,null=True)

    # filling_date = models.DateField(blank=True, null=True)
    Resume = models.FileField(blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'word'])])

    def __str__(self):
        return self.name






class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, default='')
   
    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=50,null=False, default='')
    category_name = models.ForeignKey(to=Categories,related_name='sub_category',null=True,blank=True,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.sub_category_name


class Sub_sub_category(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    sub_sub_category_name = models.CharField(max_length=50,null=False, default='')
    sub_category_name = models.ForeignKey(to=Subcategory,related_name='sub_category',null=True,blank=True,on_delete=models.CASCADE)
   

    def __str__(self):
        return self.sub_sub_category_name

class Service(models.Model):
    service_id = models.AutoField
    service_name = models.CharField(max_length=50)
    category = models.CharField(max_length=150, default="")
    category_title = models.CharField(max_length=150, default="")
    subcategory = models.CharField(max_length=150, default="")
    price = models.IntegerField(default=0)
    service_desc = models.CharField(max_length=120,)
    publish_date = models.DateField()
    Image = models.ImageField(upload_to="website/images", default="")

    def __str__(self):
        return self.service_name




class TOP(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50,default='')
    Busniess_Type = models.CharField(max_length=100,default='')
    vendor_work_desc = models.TextField(max_length=1000,default='')
    address = models.CharField(max_length=100,default='')
    state = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    vendor_mobile_no = PhoneNumberField()
    vendor_email = models.EmailField(null=True,blank=True)
    Image = models.ImageField(upload_to="website/images/TOPvendors", default="")

    

    def __str__(self):
        return self.vendor_name

    


class ServiceContact(models.Model):
    registrant_id = models.AutoField(primary_key=True)
    registrant_name =  models.CharField(max_length=50,default='')
    registrant_mobile_no = PhoneNumberField()
    registrant_interest = models.CharField(max_length=50,default='')
    registrant_query = models.TextField()


    def __str__(self):
        return self.registrant_name



STATUS_CHOICES = ( 
    ("1", "Please Select"), 
    ("2", "New"), 
    ("3", "Verified"), 
   
) 

VALID_STATE_CHOICES = (
    ("1","Please Select"),
    ("2","Andra Pradesh"),
    ("3","Arunachal Pradesh"),
    ("4","Assam"),
    ("5","Bihar"),
    ("6","Chhattisgarh"),
    ("7","Chandigarh"),
    ("8","Dadar and Nagar Haveli"),
    ("9","Daman and Diu"),
    ("10","Delhi"),
    ("11","Goa"),
    ("12","Gujarat"),
    ("13","Haryana"),
    ("14","Himachal Pradesh"),
    ("15","Jammu and Kashmir"),
    ("16","Jharkhand"),
    ("17","Karnataka"),
    ("18","Kerala"),
    ("19","Lakshadeep"),
    ("20","Madya Pradesh"),
    ("21","Maharashtra"),
    ("22","Manipur"),
    ("23","Meghalaya"),
    ("24","Mizoram"),
    ("25","Nagaland"),
    ("26","Orissa"),
    ("27","Punjab"),
    ("28","Pondicherry"),
    ("29","Rajasthan"),
    ("30","Sikkim"),
    ("31","Tamil Nadu"),
    ("32","Telagana"),
    ("33","Tripura"),
    ("34","Uttaranchal"),
    ("35","Uttar Pradesh"),
    ("36","West Bengal"),
    ("37","Andaman and Nicobar Island"),
   
)



class Vendors(models.Model):
     vendor_id = models.AutoField(primary_key=True)
     Name = models.CharField(max_length=50,default='')
     Company_Name = models.CharField(max_length=100,default='')
    #  Busniess_Type = models.CharField(max_length=1000,choices=Business_TYPES,default='Please Select')
     Busniess_Type = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='category')
     Service_decsription = models.CharField(max_length=1000,default='')
     Mobile_No = PhoneNumberField()
     Mobile_No_2 = PhoneNumberField()
     Address1 = models.CharField(max_length=100,default='')
     Address2 = models.CharField(max_length=100,blank=True,null=True,default='')
     city = models.CharField(max_length=100,default='')
     state = models.CharField(max_length=100,choices=VALID_STATE_CHOICES,default='Please Select')
     PinCode = models.IntegerField
     Contact_Person = models.CharField(max_length=100,default='',blank=True,null=True)
     EmailID = models.EmailField(null=True,blank=True)       
     Landline = PhoneNumberField(null=True)
     GST_No = models.IntegerField(null=True,blank=True)
     Pan_No = models.IntegerField(null=True,blank=True)
     TIN_No = models.IntegerField(null=True,blank=True)
     Registered_Trade_Name = models.CharField(max_length=100,blank=True,null=True,default='')
     Facebook_URL = models.URLField(max_length=200,blank=True,null=True)
     Twitter_URL = models.URLField(max_length=200,blank=True,null=True)
     website_URL = models.URLField(max_length=200,blank=True,null=True)
     Status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='New')
     Other_Info = models.CharField(max_length=200,blank=True,null=True)
     Discount_Percentage = models.IntegerField(null=True)
     Longitude = models.FloatField(null=True,blank=True)
     Latitude = models.FloatField(null=True,blank=True)
     Image = models.ImageField(upload_to="website/images/vendors", default="")


     def __str__(self):
        return self.Name

# for sbt trading form
class Trading(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    address_from = models.CharField(max_length=50)
    address_to = models.CharField(max_length=50)
    zip_code = models.IntegerField(default='')
    mobile = PhoneNumberField()

    def __str__(self):
        return self.customer_name

class Faq(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_category = models.CharField(max_length=100,default='')
    market_executive_name = models.CharField(max_length=50,default='') 
    question = models.TextField()
    answer = models.TextField()
  

    def __str__(self):
        return self.question_category


class QueryContacts(models.Model):
    query_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    mobile = PhoneNumberField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.customer_name


class Feedback(models.Model):
    customer_id = models.AutoField(primary_key=True)
    feed_back = models.CharField(max_length=50,default=False)
    Comments = models.TextField()
    customer_name = models.CharField(max_length=50,default='')
    email = models.EmailField()


    def __str__(self):
        return self.customer_name
      
class Contactviacategory(models.Model):
    registrant_id = models.AutoField(primary_key=True)
    registrant_name =  models.CharField(max_length=50,default='')
    registrant_mobile_no = PhoneNumberField()
    calling_time = models.CharField(max_length=50,default='')
    category = models.CharField(max_length=50,default='')


    def __str__(self):
        return self.registrant_name
    