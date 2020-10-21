from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.

class CustomerTestCase(APITestCase):
    def test_create_customer(self):
        url = f'/customer/CustomerAPI/'
        data = {
            "customer_name": "sads",
            "last_name": "sddsa",
            "Address": "dsads",
            "city": "sdsadsa",
            "state": "dsdsa",
            "zipcode": 4254,
            "EmailID": "sadsa",
            "gender": "dsad",
            "extra_Info": "dsad",
            "Contact_Person": "sda",
            "customer_is_active": True,
            "user": 4,
            "subscription_plan_taken": 1
        }
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

