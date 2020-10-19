# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.urls import reverse, resolve

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import User
from .serializers import *
from .functions import generate_key

import json
import pyotp
import random
import string
import requests
# from twilio.rest import Client as TwilioClient

User = get_user_model()



class UserViewSet(viewsets.ModelViewSet):
    """
    All Users Detail in list   
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class UserCreateView(viewsets.ModelViewSet):
    """
    API used for create an user after verifying from SendOtp api
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        if User.objects.filter(phone = request.data['phone']).exists():
            return Response({'User already exists Please Login and Try Again'}, status= status.HTTP_400_BAD_REQUEST)
        data = request.data
        serializer = UserCreateSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            


@api_view(['GET']) # Used for apllying api capability in function based view as above is class based!
def SendOtp(request, phno, format = None):
    """
    Functional API used for send OTP using Phone number
    """
    if not User.objects.filter(phone = phno).exists(): # there is also you can verify otp via runtime but search it out is it good or not for memory!
        totp = pyotp.TOTP('base64secret6464',interval=300)
        secret = generate_key()
        otp = totp.now()
        url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={phno}&route=TA&msgtype=1&sms=Your verifying code is {otp}"
        response = requests.request("GET",url)
        print(response)
        return Response({'sent':True,'OTP':otp})
    else:
        totp = pyotp.TOTP('base64secret6464',interval=300)
        secret = generate_key()
        otp = totp.now()
        url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={phno}&route=TA&msgtype=1&sms=Your verifying code is {otp}"
        response = requests.request("GET",url)
        print(response)
        return Response({'sent':True,'OTP':otp})
       
    

@api_view(['GET'])
def Verify(request, otpFromUser, phno):
    """
    Functional API for verifying OTP using OTP from user and Phone number
    """
    if User.objects.filter(phone = phno).exists():
        already_verified_user = User.objects.filter(phone__iexact = phno).first()
        print('...............',already_verified_user)
        count = already_verified_user.otp_count
        if count is None:
            count = 0
            totp = pyotp.TOTP('base64secret6464')
            resp = totp.verify(otpFromUser)
            already_verified_user.otp_count = count + 1
            already_verified_user.save()
            print("count increased", count)
            return Response({
                'verified': True,
                # 'User_details':already_verified_user
            })
        else:
            """if count > 10:
                return Response({
                                'status': False,
                                'detail': 'Sending OTP error. Limit exceeded. Please contact cutomer support'
                                })"""
            totp = pyotp.TOTP('base64secret6464')
            resp = totp.verify(otpFromUser)
            user = UserCreateView()
            already_verified_user.otp_count = count + 1
            already_verified_user.save()
            print("count increased", count)
            return Response({
                'verified': True,
                # 'user details':already_verified_user
            })
    totp = pyotp.TOTP('base64secret6464')
    resp = totp.verify(otpFromUser)
    user = UserCreateView()
    request.data.update({'phone':phno,'is_verified':True})
    return user.create(request)
            

         

    
    