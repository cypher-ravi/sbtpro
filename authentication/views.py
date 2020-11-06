# Create your views here.

import pyotp
import requests
from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import *

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
        data = request.data
        data['phone'] = kwargs.get('phno')
        serializer = UserCreateSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            


# @api_view(['GET']) # Used for apllying api capability in function based view as above is class based!
# def SendOtp(request, phno, format = None):
#     """
#     Functional API used for send OTP using Phone number
#     """
#     if not User.objects.filter(phone = phno).exists(): # there is also you can verify otp via runtime but search it out is it good or not for memory!
#         totp = pyotp.TOTP('base32secret3232',interval=300)
#         secret = generate_key()
#         otp = totp.now()
#         url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={phno}&route=TA&msgtype=1&sms=Your verifying code is {otp}"
#         response = requests.request("GET",url)
#         print(response)
#         print(otp)
#         return Response({'sent':True,'OTP':otp})
#     else:
#         totp = pyotp.TOTP('base32secret3232',interval=300)
#         secret = generate_key()
#         otp = totp.now()
#         url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={phno}&route=TA&msgtype=1&sms=Your verifying code is {otp}"
#         response = requests.request("GET",url)
#         print(response)
#         return Response({'sent':True,'OTP':otp})
       
    

# @api_view(['GET'])
# def Verify(request, otpFromUser, phno):
#     """
#     Functional API for verifying OTP using OTP from user and Phone number
#     """
#     if User.objects.filter(phone = phno).exists():
#         already_verified_user = User.objects.filter(phone__iexact = phno).first()
#         print('...............',already_verified_user)
#         count = already_verified_user.otp_count
#         if count == None:
#             count = 0
#             totp = pyotp.TOTP('base32secret3232')
#             resp = totp.verify(otpFromUser)
#             print(resp)
#             already_verified_user.otp_count = count + 1
#             already_verified_user.is_verified = True
#             already_verified_user.save()
#             request.data.update({'phone':phno,'is_verified':True})
#             already_verified_user = User.objects.filter(phone = phno).values()
#             return Response(already_verified_user[0],status=status.HTTP_200_OK)
#         else:
#             totp = pyotp.TOTP('base32secret3232')
#             resp = totp.verify(otpFromUser)
#             print(resp)
#             already_verified_user.otp_count = count + 1
#             already_verified_user.is_verified = True
#             already_verified_user.save()
#             request.data.update({'phone':phno,'is_verified':True})
#             already_verified_user = User.objects.filter(phone = phno).values()
#             return Response(already_verified_user[0],status=status.HTTP_200_OK)
#     totp = pyotp.TOTP('base64secret6464')
#     resp = totp.verify(otpFromUser)
#     user = UserCreateView()
#     request.data.update({'phone':phno,'is_verified':True})
#     return user.create(request)
            


    



        
class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phno):
        if not User.objects.filter(phone = phno).exists(): # there is also you can verify otp via runtime but search it out is it good or not for memory!
            totp = pyotp.TOTP('base32secret3232',interval=300)
            print('...................TOTP in send',totp)
            otp = totp.now()
            print(otp)
            url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={phno}&route=TA&msgtype=1&sms=Your verifying code is {otp}"
            response = requests.request("GET",url)
            print(response)
            print(otp)
            return Response({'sent':True,'OTP':otp})
        else:
            totp = pyotp.TOTP('base32secret3232',interval=300)
            print('...................TOTP in send else',totp)
            otp = totp.now()
            url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={phno}&route=TA&msgtype=1&sms=Your verifying code is {otp}"
            response = requests.request("GET",url)
            print(response)
            return Response({'sent':True,'OTP':otp})
        

 
    @staticmethod
    def post(request, phno):

        if User.objects.filter(phone = phno).exists():
            already_verified_user = User.objects.filter(phone__iexact = phno).first()
            print('...............',already_verified_user)
            count = already_verified_user.otp_count
            if count == None:
                count = 0
                totp = pyotp.TOTP('base32secret3232',interval=300)
                print("otp now",type(request.data['otp']))
                resp = totp.verify(request.data['otp'])  
                if resp == True:
                    already_verified_user.otp_count = count + 1
                    already_verified_user.is_verified = True
                    already_verified_user.save()
                    already_verified_user = User.objects.filter(phone = phno).values()
                   
                    print(already_verified_user[0])
                    return Response({'verified':True,'user':already_verified_user[0]},status=status.HTTP_200_OK)
                else:
                    return Response({'verified':False},status=status.HTTP_200_OK)
            else:
                totp = pyotp.TOTP('base32secret3232',interval=300)
                resp = totp.verify(request.data['otp'])
                print("otp now",type(request.data['otp']))
                print(resp)
                if resp == True:
                    already_verified_user.otp_count = count + 1
                    already_verified_user.is_verified = True
                    already_verified_user.save()
                    already_verified_user = User.objects.filter(phone = phno).values()
                    print(already_verified_user[0])
                    serializer = UserSerializer(already_verified_user[0])
                    print(serializer.data)
                    return Response({'verified':True,'user':already_verified_user[0]},status=status.HTTP_200_OK)
                else:
                    return Response({'verified':False},status=status.HTTP_200_OK)
        totp = pyotp.TOTP('base32secret3232',interval=300)
        print("otp now.................",request.data['otp'])
        resp = totp.verify(request.data['otp'])
        if resp == True:
            data = {
                'phone':phno
            }
            serializer = UserCreateSerializer(data =data )
            if serializer.is_valid(raise_exception=True):
                print('inside if.....')
                serializer.save(is_verified=True)
                return Response({'verified':True,'user':serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'verified':False})
