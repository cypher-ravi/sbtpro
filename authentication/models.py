from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.core.validators import RegexValidator
import pyotp

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free. 
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, phone, password=None, **extra_fields):
        """Create and return a `User` with an email and password."""
        
        if phone is None:
            raise TypeError('Users must have an phone number.')

        user = self.model(phone=phone, **extra_fields)
        
        user.set_password(password)
        
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password, **extra_fields):

        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(phone,password=password, **extra_fields)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


   

class Key(models.Model):
    key = models.CharField(max_length=64, unique=True, blank=True,null=True)
    is_key_activated = models.BooleanField(default=False)


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator( regex= r'^[6-9]\d{9,14}$',
                  message= "Phone number must be entered in format: '+9999999999'. Up to 14 digits allowed. ")
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    first_name = models.CharField(max_length=23, blank=True)
    key = models.ForeignKey(Key,on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default = True)# to check wheather a user is subscribed or not
    is_staff = models.BooleanField(default=False)
    is_veryfied = models.BooleanField(default=False)
    is_branch_user = models.BooleanField(default=False,blank=True,null=True)
    is_vendor = models.BooleanField(default=False,blank=True,null=True)
    is_employee = models.BooleanField(default=False,blank=True,null=True)
    is_customer = models.BooleanField(default=False,blank=True,null=True)
 
    
    
    USERNAME_FIELD = 'phone'

    objects = UserManager()
    
    class Meta:
        verbose_name ='user'
        verbose_name_plural = 'users'

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.phone

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        if self.name:
            return self.name
        else:
            return self.phone


    def get_short_name(self):
        if self.first_name:
            return self.first_name
        else:
            return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

  
    
    """def authenticate(self, otp):
        This method authenticates the given otp
        provided_otp = 0
        try:
            provided_otp = int(otp)
        except:
            return False
        #Here we are using Time Based OTP. The interval is 60 seconds.
        #otp must be provided within this interval or it's invalid
        t = pyotp.TOTP(self.key, interval=300)
        return t.verify(provided_otp)"""


"""class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex = r'^[6-9]\d{9,14}$', message = "Phone no. must be entered in format: '+9999999999', Up to 14")
    phone = models.CharField(max_length=14, validators=[phone_regex], unique=True)
    otp = models.CharField(max_length = 6, blank=True, null=True)
    is_validated = models.BooleanField(default=False)"""