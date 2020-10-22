
# Create your tests here.
import json
from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
with open("config.json", "r") as params:
    parameters = json.load(params)

class EmployeeTestCase(APITestCase):
    
    def test_create_vendor(self):
        t1 = datetime.now()
        url = f'/vendor/VendorAPI/'
        data = {
            "Name": "rv",
            "Company_Name": "fdf",
            "Service_decsription": "fdfds",
            "Mobile_No": "8010920174",
            "Mobile_No_2": "8010920174",
            "Address1": "dfds",
            "Address2": "fdsfs",
            "city": "string",
            "state": "string",
            "PinCode": 121200,
            "Contact_Person": "ravi",
            "EmailID": "ronniloreo@gmail.com",
            "Landline": "",
            "GST_No": "",
            "Pan_No": "",
            "TIN_No": "",
            "Registered_Trade_Name": "string",
            "Facebook_URL": "",
            "Twitter_URL": "",
            "website_URL": "",
            "Status": "verified",
            "Other_Info": "string",
            "Discount_Percentage": 10,
            "Longitude": 0,
            "Latitude": 0,
            "Image": "",
            "type_of_commodity_or_business": "",
            "geograpgical_area": "",
            "business_history_with_sbt": "",
            "registration_fee": ""
        }
        response = self.client.get(url,data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        t2 = datetime.now()
        time_taken_to_create_vendor = t2 - t1
        print('time_taken_to_vendor_employee',time_taken_to_create_vendor)