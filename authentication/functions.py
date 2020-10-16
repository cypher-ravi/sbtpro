from .models import User
import pyotp

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

