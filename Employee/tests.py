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
    
    def test_create_employee(self):
        t1 = datetime.now()
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
        t2 = datetime.now()
        time_taken_to_create_employee = t2 - t1
        print('time_taken_to_create_employee',time_taken_to_create_employee)


class DailyAttendanceTestCase(APITestCase):
    def test_daily_attendance_if_punch_time_is_true(self):
        key = parameters['key']
        url = f'employee:attendance_post_request'
        data = {
            "id": 19,
            "punching_in": "True",
            "vendor": "racu",
            "work_description": "sdas",
            "longitude": "dasd",
            "latitude": "4324.324",
            "user": 14,
            'punch_time':'4242542',
            'punching_out_time' : ''

        }
        response = self.client.post(reverse(url,args=['key']),data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_daily_attendance_if_punch_time_is_false(self):
        key = parameters['key']
        url = f'employee:attendance_post_request'
        data = {
            "id": 19,
            "punching_in": "False",
            "vendor": "racu",
            "work_description": "sdas",
            "longitude": "dasd",
            "latitude": "4324.324",
            "user": 14,
            'punch_time':'',
            'punching_out_time' : ''

        }
        response = self.client.post(reverse(url,args=['key']),data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_check_if_user_exists(self):
        key = parameters['key']
        url = f'employee:attendance_post_request'
        data = {
            "id": 19,
            "punching_in": "False",
            "vendor": "racu",
            "work_description": "sdas",
            "longitude": "dasd",
            "latitude": "4324.324",
            "user": 55,
            'punch_time':'',
            'punching_out_time' : ''

        }
        response = self.client.post(reverse(url,args=['key']),data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
