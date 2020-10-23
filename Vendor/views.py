from django.shortcuts import render ,HttpResponse,get_list_or_404,get_object_or_404
from rest_framework import viewsets,generics
from rest_framework import permissions,status,mixins
from rest_framework.response import Response 

from django.contrib.auth import get_user_model
from .models import VendorServices,VendorVideos,Vendor
from .pagination import PaginationForVendor
from .serializers import VendorListSerializer,VendorSerializer,VendordetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from sbt.settings.base import REST_FRAMEWORK
import json
from django.views.generic import ListView

User = get_user_model()
with open("config.json", "r") as params:
    parameters = json.load(params)


# Create your views here.
# class VendorList(generics.GenericAPIView):
class VendorList(viewsets.ModelViewSet):

    """
    List of all Vendor by category ID

    """
    model = Vendor
    serializer_class = VendorListSerializer
    pagination_class = PaginationForVendor
    allow_empty = False
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):  # no pk parameter
        key = parameters['key']
        if not key == self.kwargs['slug']:
            return Vendor.objects.none()
        else:
            category = self.kwargs['pk']
            return Vendor.objects.filter(Busniess_Type=category)
        

class VendorDetail(generics.GenericAPIView):
    """
    Vendor Detail By user ID

    """
    queryset = Vendor.objects.all()
    serializer_class = VendordetailSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,slug,pk, format=None):
        vendor = Vendor.objects.filter(user=pk)
        print(vendor)
        if vendor.exists():
            key = parameters['key']
            if slug == key:   
                serializer = VendordetailSerializer(vendor[0],many=False)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':'user not exists'})
        

class NewVendorAPI(viewsets.ModelViewSet):
    """
    This API creates new vendor and delete,update via id using viewsets

    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        vendor = Vendor.objects.filter(Company_Name__iexact = request.data['Company_Name'])
        if vendor.exists():
            return Response({'detail':'vendor already exists'},status=status.HTTP_400_BAD_REQUEST) 
        data = request.data
        serializer = VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
