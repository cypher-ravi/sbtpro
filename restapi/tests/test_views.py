from django.test import TestCase
from django.urls import reverse,path,include
from rest_framework import status
from rest_framework.test import APITestCase,URLPatternsTestCase
from website.models import Vendor,Categories
from dashboard.models import *
import os
import io
from PIL import Image

# Create your tests here.
img = Image.open('restapi/tests/adeolu-eletu-unRkg2jH1j0-unsplash_copy.jpg')

class EmployeeViewTest(APITestCase,URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('restapi.urls')),
    ]
    def test_create_employee(self):
        """
        Ensure we can create a new employee object
        """
        url = reverse('rest_api:employee-list')
        
        # Send data
        
        data = {
            "employee_id": 4,
            "employee_name": "ravibeniwal",
            "father_name": "dsd",
            "Mobile_No": "+918010920174",
            "Mobile_No_2": "+918010920174",
            "Address1": "202  parvatiya colony, fbd",
            "Address2": "da",
            "city": "Faridabad",
            "state": "13",
            "zipcode": 121005,
            "country": "IN",
            "EmailID": "test@test.com",
            "joining_date": "2020-10-13T20:25:06.213141+05:30",
            "gross_salary": 4565241,
            "gender": "2",
            "date_of_birth": "2020-10-01",
            "extra_Info": "xczx",
            "Contact_Person": "Xz",
            "employee_is_active": True,
            "employee_designation": "Android Developer",
            "Image": img
            }
        
        response = self.client.post(url,data,format='multipart')
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().employee_name, 'ravibeniwal')

