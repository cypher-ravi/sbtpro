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


class Service(models.Model):
    service_id = models.AutoField
    service_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    category_title = models.CharField(max_length=150, default="")
    Subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    service_desc = models.CharField(max_length=120,)
    publish_date = models.DateField()
    Image = models.ImageField(upload_to="website/images", default="")

    def __str__(self):
        return self.service_name


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
    name = models.CharField(max_length=50, default='')

    # filling_date = models.DateField(blank=True, null=True)
    Resume = models.FileField(blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'word'])])

    def __str__(self):
        return self.name


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, default='')
    sub_category_name1 = models.CharField(max_length=50,null=True, default='')
    sub_category_name2 = models.CharField(max_length=50, default='',null=True)
    sub_category_name3 = models.CharField(max_length=50, default='',null=True)
    sub_category_name4 = models.CharField(max_length=50, default='',null=True)
    sub_category_name5 = models.CharField(max_length=50, default='',null=True)
    sub_category_name6 = models.CharField(max_length=50, default='',null=True)
    sub_category_name7 = models.CharField(max_length=50, default='',null=True)
    sub_category_name8 = models.CharField(max_length=50, default='',null=True)
    sub_category_name9 = models.CharField(max_length=50, default='',null=True)
    sub_category_name10 = models.CharField(max_length=50, default='',null=True)

    def __str__(self):
        return self.category_name




class TOP(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50,default='')
    vendor_work_desc = models.CharField(max_length=1000,default='')
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
    registrant_query = models.CharField(max_length=500,default='')


    def __str__(self):
        return self.registrant_name

