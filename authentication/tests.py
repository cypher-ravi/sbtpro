import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User
from authentication.serializers import UserCreateSerializer, UserSerializer
from authentication.views import SendOtp,Verify,UserCreateView
# Create your tests here.

class UserCreationTestCase(APITestCase):
    def test_send_otp(self):
        # data = {
        #     'phone':'8683827390',
        # }
        
        url = 'send_sms_code/8683827390'
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
