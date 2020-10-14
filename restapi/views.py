from website.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from django.http import Http404,HttpResponseServerError
from django.conf import settings
import json
from django.shortcuts import get_object_or_404



with open("D:\workspace sbt\deployment\prodsbt\config.json", "r") as params:
    parameters = json.load(params)



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

    
class BannersList(APIView):
    """
    List of all Banners

    """
    def get(self, request,slug, format=None):
        key = parameters['key']
        if slug == key:
            banner = Banner.objects.all()
            serializer = AllBannerSerializer(banner, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class VendorDetail(generics.GenericAPIView):
    """
    Vendor Detail By ID

    """
    serializer_class = VendorListSerializer
    queryset = Vendor
    def get(self, request,vendor_id,slug, format=None):
        key = parameters['key']
        if slug == key:
            vendor = Vendor.objects.filter(vendor_id=vendor_id)
           
            serializer = VendorListSerializer(vendor, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request,vendor_id,slug, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST) 

class PlanList(APIView):
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





class PlanDetail(generics.GenericAPIView):
    """
    Plan Detail By ID

    """
    serializer_class = CustomerPlanSerializer
    queryset = Plan
    def get(self, request,plan_id,slug, format=None):
        key = parameters['key']
        if slug == key:
            plan = Plan.objects.filter(plan_id=plan_id)
           
            serializer = CustomerPlanSerializer(plan, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class EmployeeDailyAttendanceDetail(generics.GenericAPIView):
    """
    Employee Attendance Detail By ID

    """
    serializer_class = DailyAttendanceSerializer
    queryset = DailyAttendance
    def get(self, request,employee_id,slug, format=None):
        key = parameters['key']
        if slug == key:
            attendance = DailyAttendance.objects.filter(employee=employee_id)
            serializer = DailyAttendanceSerializer(attendance, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AttendanceList(generics.ListCreateAPIView):
    queryset = DailyAttendance.objects.all()
    serializer_class = DailyAttendanceSerializer
    

    
"""   
--------------------------------------------ViewSets----------------------------------------------------------                  
"""
class NewCategoryAPI(viewsets.ModelViewSet):
    """
    This API creates new category and delete,update via id using viewsets

    """
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class NewEmployeeAPI(viewsets.ModelViewSet):
    """
    This API creates new employee and delete,update via id using viewsets

    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        employee = Employee.objects.filter(employee_name=request.data['employee_name'])
        if employee.exists():
            return Response({'detail':'Employee already exists'},status=status.HTTP_400_BAD_REQUEST) 
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    



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


class ToptList(viewsets.ModelViewSet):
    """
    This API creates new Top,view and edit using viewsets

    """
    queryset = TOP.objects.all()
    serializer_class = TOPSerializer

    def create(self, request, *args, **kwargs):
        top = TOP.objects.filter(vendor_name=request.data['vendor_name'])
        if top.exists():
            return Response({'detail':'TOP vendor already exists'},status=status.HTTP_400_BAD_REQUEST) 
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
class NewCustomerAPI(viewsets.ModelViewSet):
    """
    This API creates new Customer,view and edit using viewsets

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        customer = Customer.objects.filter(customer_name=request.data['customer_name'])
        if customer.exists():
            return Response({'detail':'customer already exists'},status=status.HTTP_306_RESERVED) 
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DailyAttendanceAPI(viewsets.ModelViewSet):
#     """
#     This API creates new attendance,view and edit using viewsets

#     """
#     queryset = DailyAttendance.objects.all()
#     serializer_class = DailyAttendanceSerializer

#     def create(self, request,employee_id, *args, **kwargs):
#         attendance = DailyAttendance.objects.filter(employee=employee_id)
#         data = request.data
#         serializer = DailyAttendanceSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)