import json

from Customer.serializers import CustomerPlanSerializer
from dashboard.models import Banner
from dashboard.serializers import AllBannerSerializer
from django.conf import settings
from django.http import Http404, HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from Vendor.models import Vendor
from Vendor.serializers import VendorListSerializer, VendorSerializer
from website.models import Categories, Plan

from .serializers import *

with open("config.json", "r") as params:
    parameters = json.load(params)

from authentication.pagination import PaginationForVendorAndCategory
from django_filters.rest_framework import DjangoFilterBackend


class VendorList(generics.ListAPIView):
    """
    API filter Vendors by Category,Company Service decsription ,vendor services
    Use these fields for search Busniess_Type Service_decsription vendor_services
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Busniess_Type', 'Service_decsription','vendor_services','Address1','city','state','Company_Name','Name']
    



class FrenchiseRequestAPIView(generics.CreateAPIView):
    """
    This API accepts post requests for frenchise requests 
    """
    queryset = FrenchiseContact.objects.all()
    serializer_class = FrenchiseRequestSerializer

    def post(self, request, format=None):
        key = parameters['key']
        # if slug == key:
        serializer = FrenchiseRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'You are not allowed to access these end points'}, status=status.HTTP_400_BAD_REQUEST)

        





          

 #--------------------------------------------ViewSets----------------------------------------------------------                  
 
class NewCategoryAPI(viewsets.ModelViewSet):
    """
    This API creates new category and delete,update via id using viewsets

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
