from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.

class CustomerTestCase(APITestCase):
    def test_create_customer(self):
        url = f'/customer/CustomerAPI/'
        data = {
            'customer_name':'ravi',
            'last_name':'kumar',
            'Address':'fbd',
            'city':'ravi',
            'state':'Haryana',
            'zipcode':121005,
            'EmailID':'ronniloreo@gmail.com',
            'gender':'',
            'extra_Info':'ravi',
            'Contact_Person':'ravi',
            'customer_is_active':False,
            'subscription_plan_taken':'',
            'user':4,
        }
        response = self.client.post(url,data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

