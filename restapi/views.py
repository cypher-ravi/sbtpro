import json

import requests
from Customer.serializers import CustomerPlanSerializer
from dashboard.models import Banner
from dashboard.serializers import AllBannerSerializer
from django.conf import settings
from django.http import Http404, HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.metadata import SimpleMetadata
from rest_framework.response import Response
from rest_framework.views import APIView
from Vendor.models import Vendor
from Vendor.serializers import *
from website.models import Categories, Plan
from Vendor.pagination import PaginationForVendor

from .serializers import *

with open("config.json", "r") as params:
    parameters = json.load(params)

from authentication.pagination import PaginationForVendorAndCategory
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



    
class CategorySearchView(generics.ListAPIView):
    """
    Search API for categroies 
    """
    queryset = Categories.objects.all()
    pagination_class = PaginationForVendorAndCategory
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name']

class VendorSearchView(generics.ListAPIView):
    """
    Search API for vendors + category_id
    """
    
    pagination_class = PaginationForVendor
    serializer_class = VendorSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Company_Name']

    def get_queryset(self):
        vendors = Vendor.objects.filter(Busniess_Type=self.kwargs['category_id'])
        return vendors



class FrenchiseRequestAPIView(generics.CreateAPIView):
    """
    This API accepts post requests for franchise requests 
    """
    queryset = FrenchiseContact.objects.all()
    serializer_class = FrenchiseRequestSerializer
    metadata_class = SimpleMetadata

    def post(self, request, format=None):
        key = parameters['key']
        # if slug == key:
        serializer = FrenchiseRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            name = request.data['name']
            mobile_no = request.data['mobile_no']
            email = request.data['email']
            address = request.data['address']
            frenchise_option = request.data['franchise_option']
            company_name = request.data['company_name']
            message = request.data['message']
            url = f'http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={+918683827398}&route=TA&msgtype=1&sms=New Frenchise request \n\nName ={name} \nMobile= {mobile_no} \nEmail= {email}\nAddress= {address} \nFrenchise option= {frenchise_option} \nMessage= {message} \nCompany Name= {company_name}'
            response = requests.request("GET",url)
            return Response({'sent':'True'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class AppFeedBackAPIView(generics.CreateAPIView):
    """
    This API accepts post requests for Feedback 
    """
    queryset = AppFeedBack.objects.all()
    serializer_class = AppFeedBackSerializer
    metadata_class = SimpleMetadata

    def post(self, request, format=None):
        key = parameters['key']
        # if slug == key:
        serializer = AppFeedBackSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'sent':'True'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





          

 #--------------------------------------------ViewSets----------------------------------------------------------                  
 
class NewCategoryAPI(viewsets.ModelViewSet):
    """
    This Paginated API creates new category and delete,update via id using viewsets

    """
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PaginationForVendorAndCategory
    
   



class ToptList(viewsets.ReadOnlyModelViewSet):
    """
    This API creates new Top,view and edit using viewsets

    """
    queryset = TOP.objects.all()
    serializer_class = TOPSerializer

    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:
            top = TOP.objects.all()
            serializer = TOPSerializer(top,many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class PlanList(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = CustomerPlanSerializer
    """
    List of all Plans

    """
    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:
            plan = Plan.objects.all()
            serializer = CustomerPlanSerializer(plan,many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PlanDetail(viewsets.ReadOnlyModelViewSet):
    """
    Plan Detail By ID

    """
    serializer_class = CustomerPlanSerializer
    queryset = Plan.objects.all()
    
    def get(self, request,plan_id,slug, format=None):
        key = parameters['key']
        if slug == key:
            serializer = CustomerPlanSerializer(plan, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class BannersList(viewsets.ReadOnlyModelViewSet):
    """
    List of all Banners

    """
    queryset = Banner.objects.all()
    serializer_class = AllBannerSerializer

    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:
            serializer = AllBannerSerializer(banner, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
