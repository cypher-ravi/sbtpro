from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from django.shortcuts import render,redirect
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .functions import generate_key
import pyotp
import random
import string

from django.urls import reverse, resolve

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



"""
class PhoneNumberView(ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneSerializer"""

class UserCreateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        print('............................',request)
        if User.objects.filter(phone = request.data['phone']).exists():
            return Response({'User already exists Please Login and Try Again'}, status= status.HTTP_400_BAD_REQUEST)
        data = request.data
        serializer = UserCreateSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'User Created Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            


@api_view(['GET']) # Used for apllying api capability in function based view as above is class based!
def SendOtp(request, phno, format = None):
    if not User.objects.filter(phone = phno).exists(): # there is also you can verify otp via runtime but search it out is it good or not for memory!
        totp = pyotp.TOTP('base64secret6464')
        print('............',totp)
        secret = generate_key()
        otp = totp.now()
        return Response({'OTP':otp, 'key':secret})
    return Response({'Phone already verified!'})
    

@api_view(['GET'])
def Verify(request, otpFromUser, phno):
    if User.objects.filter(phone = phno).exists():
        return Response({'Phone number already verified'})
    totp = pyotp.TOTP('base64secret6464')
    resp = totp.verify(otpFromUser)
    user = UserCreateView()
    request.data.update({'phone':phno})
    print('..........', request.data)
    # print('......',request.data['phone'])
    # return UserCreateView.as_view({'get':'list'})(request)
    return user.create(request)

    
    



"""
def generate_key():
    x = string.ascii_letters + string.digits + string.punctuation
    key = ''.join([random.choice(x) for _ in range(64)])
    return key
"""