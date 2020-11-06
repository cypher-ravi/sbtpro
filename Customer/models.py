from dashboard.models import Branch
from django.contrib.auth import get_user_model
from django.db import models
from website.models import Plan

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




class Customer(models.Model):
    """
    Model for customer, this model uses after API used to create customer
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True, blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=20,default='',null= True, blank=True)
    last_name = models.CharField(max_length=20,default='',blank=True,null=True)
    Address = models.CharField(max_length=100, default='',null= True, blank=True)
    city = models.CharField(max_length=100, default='',null= True, blank=True)
    state = models.CharField(max_length=100,default='',null= True, blank=True)
    zipcode = models.IntegerField(null= True, blank=True)
    EmailID = models.CharField(max_length=50,null=True, blank=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=100, default='',null=True,blank=True)
    extra_Info = models.TextField(max_length=200, blank=True, null=True)
    Contact_Person = models.CharField(max_length=100, default='', blank=True, null=True)
    customer_is_active = models.BooleanField(default=False)
    subscription_plan_taken = models.ForeignKey('website.Plan',on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering = ['customer_id']

    def __str__(self):
        return self.customer_name

