from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


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

# # Create your models here.
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