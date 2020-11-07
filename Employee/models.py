from dashboard.models import Branch
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

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


# # Create your models here.


class Employee(models.Model):
    """
    Model associate with vendor and branch,
    this model create employee after form fill up by user role panel in APP
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True, blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100,default='',blank=True,null=True)
    last_name = models.CharField(max_length=20,default='',blank=True,null=True)
    father_name = models.CharField(max_length=100,default='',blank=True,null=True)
    Mobile_No = models.CharField(max_length=14,blank=True,null=True)
    Mobile_No_2 = models.CharField(max_length=14,blank=True,null=True)
    Address1 = models.CharField(max_length=500, default='',blank=True,null=True)
    Address2 = models.CharField(max_length=500, blank=True, null=True, default='')
    city = models.CharField(max_length=100, default='',blank=True,null=True)
    state = models.CharField(max_length=100, default='',blank=True,null=True)
    zipcode = models.IntegerField(blank=True,null=True)
    EmailID = models.CharField(max_length=50,null=True, blank=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    gross_salary = models.BigIntegerField(blank=True,null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='Please Select',blank=True,null=True)
    date_of_birth = models.CharField(max_length=10,blank=True,null=True)
    extra_Info = models.TextField(max_length=200, blank=True, null=True)
    Contact_Person = models.CharField(max_length=100, default='', blank=True, null=True)
    employee_is_active = models.BooleanField(default=False,blank=True,null=True)
    employee_designation = models.CharField(max_length=30,default='',blank=True,null=True)
    Image = models.ImageField(upload_to="dashboard/images/Employee", blank=True,null=True)
    qualification = models.CharField(max_length=100,default='',blank=True,null=True)
    university = models.CharField(max_length=150,default='',blank=True,null=True)
    year_of_passing = models.CharField(max_length=30,default='',blank=True,null=True)
    education_percentage = models.CharField(max_length=30,default='',blank=True,null=True)

    def __str__(self):
        return str(self.employee_name)


class DailyAttendance(models.Model):
    """
    Model used for punch daily attendance by Employee
    """
    ATTENDACE_CHOICES = (
    ("True", "True"),
    ("False", "False"),

    )
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)

    punching_in = models.CharField(max_length=20,choices=ATTENDACE_CHOICES,default='False')
    punch_time = models.DateTimeField(auto_now_add=True)
    punching_out_time = models.CharField(max_length=50,default='')
    vendor = models.CharField(max_length=50,null=True,blank=True)
    work_description = models.TextField(max_length=1000,null=True,blank=True)
    longitude = models.CharField(max_length=100,null=True,blank=True)
    latitude = models.CharField(max_length=100,null=True,blank=True)
    user = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.employee) + ' today punch time is ' + str(self.punch_time)
