from django.shortcuts import render

from rest_framework import viewsets,generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from .models import Employee,DailyAttendance
from .serializers import EmployeeSerializer,DailyAttendanceSerializer

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
class NewEmployeeAPI(viewsets.ModelViewSet):
    """
    This API creates new employee and delete,update via id using viewsets

    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        employee = Employee.objects.filter(employee_name=request.data['employee_name'])
        if employee.exists():
            return Response({'detail':'Employee already exists'},status=status.HTTP_400_BAD_REQUEST) 
        data = request.data
        user_data = request.data['user']
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.filter(id=request.data['user'])
            for employee in user:
                employee.is_employee_registered = True
                employee.save()
            user = User.objects.filter(id=request.data['user']).values()
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

            
         
    

class EmployeeDailyAttendanceDetail(generics.GenericAPIView):
    """
    Employee Attendance Detail By ID

    """
    serializer_class = DailyAttendanceSerializer
    queryset = DailyAttendance
    # permission_classes = [permissions.IsAuthenticated]

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
    