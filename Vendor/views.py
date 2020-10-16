from django.shortcuts import render ,HttpResponse
from rest_framework import viewsets
from .models import VendorServices,VendorVideos,Vendor
from .serializers import VendorListSerializer,VendorSerializer

# Create your views here.
class VendorList(viewsets.ReadOnlyModelViewSet):
    """
    List of all Vendor

    """
    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer

    def get(self, request,category_id,slug, format=None):
        key = parameters['key']
        if slug == key:
            vendor = Vendor.objects.filter(Busniess_Type=category_id)
            serializer = VendorListSerializer(vendor, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class VendorDetail(viewsets.ReadOnlyModelViewSet):
    """
    Vendor Detail By ID

    """
    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer
    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:   
            serializer = VendorListSerializer(many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class NewVendorAPI(viewsets.ModelViewSet):
    """
    This API creates new vendor and delete,update via id using viewsets

    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

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
