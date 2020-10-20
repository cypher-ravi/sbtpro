import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User
from authentication.serializers import UserCreateSerializer, UserSerializer
from authentication.views import SendOtp,Verify,UserCreateView
import pyotp
# Create your tests here.

class UserCreationTestCase(APITestCase):
    def test_send_otp(self):
        phone = ['8683827390']
        
        url = f'authentication:SendOtp'
        response = self.client.get(reverse(url,args=phone))
        self.assertEqual(response.status_code,status.HTTP_200_OK)




