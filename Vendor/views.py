import base64
import io
import pathlib

from django.http.response import HttpResponse, JsonResponse
from Vendor.functions import assign_branch_to_vendor
#  convert_to_image_and_save_to_VendorImages
import json

from django.contrib.auth import get_user_model

from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from sbt.settings.base import REST_FRAMEWORK
from rest_framework.parsers import FormParser ,MultiPartParser 

from .models import Vendor, VendorImages, VendorServices
from .pagination import PaginationForVendor
from .serializers import (VendorImageAPISerializer, VendorImagesListSerializer, VendorServiceAPISerializer, VendorServiceListSerializer, VendordetailSerializer, VendorListSerializer,
                          VendorSerializer)

User = get_user_model()
fn = pathlib.Path(__file__).parent.parent / 'config.json'
with open(fn,"r") as params:
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
    parser_class = (MultiPartParser,FormParser)
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        create vendor  by User ID
        """
        vendor = Vendor.objects.filter(
            user=request.data['user'])
        if vendor.exists():
            vendor = Vendor.objects.filter(user=request.data['user']).first()
            partial = kwargs.pop('partial', True)
            instance = vendor
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            return Response({'details':'updated'})
        data = request.data
        user = User.objects.filter(id=request.data['user'])
        for check_vendor in user:
            if check_vendor.is_vendor_registered == True:
                return Response('this user already a vendor')
        serializer = VendorSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            for cust in user:
                cust.is_vendor_registered = True
                cust.save()
            user = User.objects.filter(id=request.data['user']).values()
            assign_branch_to_vendor(request.data['city'],request.data['state'],request.data['user'])
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




class VendorImageAPIView(viewsets.ModelViewSet):
    """
    Image Upload by user Id
    """
    queryset = VendorImages.objects.all()
    serializer_class = VendorImageAPISerializer
    parser_class = (MultiPartParser,FormParser)

    def create(self,request, *args, **kwargs):
        vendor = Vendor.objects.filter(user=request.data['user'])
        if vendor.exists():
            serializer = VendorImageAPISerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(vendor=vendor[0])
                return JsonResponse(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([])
        




class VendorImageDetailView(generics.GenericAPIView,mixins.DestroyModelMixin):
    """
    Vendor Image Detail By user ID

    """
    queryset = VendorImages.objects.all()
    serializer_class = VendorImagesListSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,slug,pk, format=None):
        vendor_images = VendorImages.objects.filter(user=pk)
        if vendor_images.exists():
            key = parameters['key']
            if slug == key:   
                serializer = VendorImagesListSerializer(vendor_images,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)           
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([])



class VendorServiceAPIView(viewsets.ModelViewSet):
    """
    Post API for vendor services
    """
    queryset = VendorServices.objects.all()
    serializer_class = VendorServiceAPISerializer

    def create(self,request, *args, **kwargs):
        try:
            vendor = Vendor.objects.filter(user=request.data['user'])
        except:
            return Response([])
        if vendor.exists():
            serializer = VendorServiceAPISerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(vendor=vendor[0])
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([])
        
  


class VendorServiceDetailView(generics.GenericAPIView,mixins.DestroyModelMixin):
    """
    Vendor Service Detail By user ID

    """
    queryset = VendorServices.objects.all()
    serializer_class = VendorServiceListSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,slug,pk, format=None):
        vendor_services = VendorServices.objects.filter(user=pk)
        if vendor_services.exists():
            key = parameters['key']
            if slug == key:   
                serializer = VendorServiceListSerializer(vendor_services,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)          
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([])



class VendorImagesByVendorID(generics.GenericAPIView):

    queryset = VendorServices.objects.all()
    serializer_class = VendorImagesListSerializer

    def get(self, request,slug,pk, format=None):
        vendor_images= VendorImages.objects.filter(vendor__vendor_id=pk)
        if vendor_images.exists():
            key = parameters['key']
            if slug == key:   
                serializer = VendorImagesListSerializer(vendor_images,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)                
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([])



class VendorServicesByVendorID(generics.GenericAPIView):
    """
    Vendor services by vendor ID
    """
    
    queryset = VendorServices.objects.all()
    serializer_class = VendorServiceListSerializer

    def get(self, request,slug,pk, format=None):
        vendor_service= VendorServices.objects.filter(vendor__vendor_id=pk)
        if vendor_service.exists():
            key = parameters['key']
            if slug == key:   
                serializer = VendorServiceListSerializer(vendor_service,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)        
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([])




def add_user_to_vendor(request):
    vendors = Vendor.objects.all()
    vendor = []
    for i in vendors:

        vendor.append(i.Mobile_No)
        user = User.objects.get_or_create(phone=i.Mobile_No,is_vendor_registered=True,is_vendor_paid=True)
        user.save()
        i.user = user
        i.save()
    return HttpResponse(vendor)

