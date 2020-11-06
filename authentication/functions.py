from .models import User
import pyotp
import math
import random


def generate_key():
    """ User otp key generator """
    key = pyotp.random_base32()
    return key

    
# def is_unique(key):
#     try:
#         User.objects.get(key=key)
#     except User.DoesNotExist:
#         return True
#     return False

def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # length of password can be chaged 
   # by changing value in range 
    for i in range(6) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP