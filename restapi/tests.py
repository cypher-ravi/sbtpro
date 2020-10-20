import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

with open("config.json", "r") as params:
    parameters = json.load(params)

class BannerListTestCase(APITestCase):
    """
    This Test will check response of banners list API  
    """
    def test_banner_list(self):
        key = parameters['key']
        url = f'rest_api:banners_list'
        response = self.client.get(reverse(url,args=['key']))
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class TopsListTestCase(APITestCase):
    """
    This Test will check response of Team Of Professionals list API  
    """
    def test_tops_list(self):
        key = parameters['key']
        url = f'rest_api:tops_list'
        response = self.client.get(reverse(url,args=['key']))
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class PlanListTestCase(APITestCase):
    """
    This Test will check response of Plans list API  
    """
    def test_plans_list(self):
        key = parameters['key']
        url = f'rest_api:plan_list'
        response = self.client.get(reverse(url,args=['key']))
        self.assertEqual(response.status_code,status.HTTP_200_OK)


"""class SearchAPITestCase(APITestCase):
    # This Test will check response of Search API  
    # by vendor name ,business type ,service description ,
    # address ,city ,state ,companyname

    def test_search(self):
        key = parameters['key']
        url = f'rest_api:search_api'
        data = {
            'Busniess_Type':13,
            'Service_decsription':'',
            'vendor_services':5,
            'Address1':'',
            'city':'',
            'state':'Haryana',
            'Company_Name':'',
            'Name':''
        }
        response = self.client.get(reverse(url,args=['key']),data=data)
        print('this is response',response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
"""

class FrenchiseRequestTestCase(APITestCase):
    """
    This Test will check response of Frenchise requests API  
    """
    def test_fernchise_request(self):
        key = parameters['key']
        url = f'rest_api:frenchise_request'
        data = {
            "name": "hlo",
            "mobile_no": "668586786",
            "email": "xzcx",
            "address": "cxcxczxc",
            "frenchise_option": "czxcxzc",
            "company_name": "xczxczx",
            "message": "czxcxczx",

        }
        response = self.client.post(reverse(url),data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
