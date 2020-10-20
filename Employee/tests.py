from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.


class EmployeeTestCase(APITestCase):
    def test_create_employee(self):
        url = f'/employee/EmployeeAPI/'
        data = {
            'user':19,
            'employee_name':'ravidummy',
            'last_name':'oreo',
            'father_name':'dsdf',
            'Mobile_No':'8010920174',
            'Address1':'h.no 202,parvatiya colony',
            'city':'faridabad',
            'state':'Haryana',
            'zipcode':121005,
            'EmailID':'ronniloreo@gmail.com',
            'gross_salary':'200000',
            'date_of_birth':'3/12/1999',
            'qualification':'B.tech',
            'university':'VJTI college of mumbai',
            'year_of_passing':'2020',
            'education_percentage':'99',
        }
        response = self.client.get(url,data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
