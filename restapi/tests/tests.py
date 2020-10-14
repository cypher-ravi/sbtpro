from django.test import TestCase
from django.urls import reverse,path,include
from rest_framework import status
from rest_framework.test import APITestCase,URLPatternsTestCase
from website.models import Vendor,Categories

# Create your tests here.

# class VendorViewTest(APITestCase,URLPatternsTestCase):
#     urlpatterns = [
#         path('api/', include('restapi.urls')),
#     ]
#     def test_create_vendor(self):
#         """
#         Ensure we can create a new vendor object
#         """
#         url = reverse('rest_api:vendor-list')
#         data ={
#             "vendor_id": 6,
#             "Name": "sbtprofessionals",
#             "Company_Name": "eter",
#             "Service_decsription": "retret",
#             "Mobile_No": "+918010920174",
#             "Mobile_No_2": "+918010920174",
#             "Address1": "test",
#             "Address2": "sfs",
#             "city": "sds",
#             "state": "13",
#             "PinCode": 12454,
#             "Contact_Person": "",
#             "EmailID": "test@gmail.com",
#             "Registered_Trade_Name": "",
#             "Facebook_URL": "",
#             "Twitter_URL": "",
#             "website_URL": "",
#             "Status": "1",
#             "Other_Info": "",
#             "Discount_Percentage": 23,
#             "submit_date": "2020-10-14T14:38:23.904445+05:30",
#             "Image": "/media/website/images/vendors/IT.jpg",
#             "type_of_commodity_or_business": "distrubution",
#             "geograpgical_area": "tehsil",
#             "business_history_with_sbt": "YES",
#             "registration_fee": "INR 1200/per month",
#             "Busniess_Type": Categories.category_id[0],
#             "vendor_video": ,
#             "vendor_services": [
#                 1
#             ]
#         }
        
#         response = self.client.post(url,data,format='json')
#         print(response.data)
#         self.assertEqual(response.status_code,status.HTTP_201_CREATED)
#         self.assertEqual(Vendor.objects.count(), 6)
#         self.assertEqual(Vendor.objects.get().Company_Name, 'eter')

