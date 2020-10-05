from website.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404,HttpResponseServerError
from django.conf import settings
import json




with open("D:\workspace sbt\deployment\prodsbt\config.json", "r") as params:
    parameters = json.load(params)



# api_key = parameters["key"]

class ToptList(APIView):
    """
    List all vendors.
    """
    def get(self, request,slug, format=None):
        tops = TOP.objects.all()
        serializer = TOPSerializer(tops, many=True)
        value = 'asdfghjkl'
        if slug == value:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
                

            
class CategoryList(APIView):
    """
    List of all Categories

    """
    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:
            categories = Categories.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class VendorList(APIView):
    """
    List of all Vendor

    """
    def get(self, request,category_id,slug, format=None):
        key = parameters['key']
        if slug == key:
            vendor = Vendor.objects.filter(Busniess_Type=category_id)
            serializer = VendorListSerializer(vendor, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VendorDetail(APIView):
    """
    Vendor Detail By ID

    """
    def get(self, request,vendor_id,slug, format=None):
        key = parameters['key']
        if slug == key:
            vendor = Vendor.objects.filter(vendor_id=vendor_id)
            serializer = VendorDetailSerializer(vendor, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

