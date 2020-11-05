from Employee.functions import assign_branch_to_employee
import json
from datetime import datetime

from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets,mixins
from rest_framework.response import Response

from .models import DailyAttendance, Employee
from .serializers import DailyAttendanceSerializer, EmployeeSerializer

User = get_user_model()
# Create your views here.

with open("config.json", "r") as params:
    parameters = json.load(params)



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
            employee = Employee.objects.filter(
            user=request.data['user']).first()
            if employee != None:
                partial = kwargs.pop('partial', False)
                instance = employee
                serializer = self.get_serializer(instance, data=request.data, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)

                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}

                return Response({'details':'updated'})
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
            #for check if vendor is active
            assign_branch_to_employee(request.data['city'],request.data['state'],request.data['user'])
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

            
         
    

class EmployeeDailyAttendanceDetail(generics.GenericAPIView):
    
    serializer_class = DailyAttendanceSerializer
    queryset = DailyAttendance
    # permission_classes = [permissions.IsAuthenticated]
    

    def post(self, request, *args, **kwargs):
        employee_from_user = Employee.objects.filter(user=request.data['user'])
        if employee_from_user.exists():
            employee = DailyAttendance.objects.filter(employee=employee_from_user[0])
            data = request.data
            punching_in = request.data['punching_in']
            if punching_in == 'True':
                serializer = DailyAttendanceSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(employee=employee_from_user[0])
                    return Response({'Attendance marked':'True'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors)
            else:
                employee = DailyAttendance.objects.filter(employee=employee_from_user[0])
                for em in employee:
                    if em.punch_time == 'False':
                        return Response({'detail':'Punch in before punchout'})
                    em.punching_out_time = datetime.now()
                    em.save()
                    return Response({'punch out time':'ok'})
        return Response({'Detail':'User not exists'})


                
        
                    

class EmployeeDailyAttendanceList(generics.ListAPIView):
    """
    List of daily attendance by employee id

    """
    queryset = DailyAttendance.objects.all()
    serializer_class = DailyAttendanceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request,pk,slug, format=None):
        key = parameters['key']
        if slug == key:
            employee = DailyAttendance.objects.filter(employee=pk)
            serializer = DailyAttendanceSerializer(employee, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




        
    

class AttendanceList(generics.ListCreateAPIView):
    queryset = DailyAttendance.objects.all()
    serializer_class = DailyAttendanceSerializer
    





class EmployeeDetail(generics.GenericAPIView):
    """
    Employee Detail By user ID

    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,slug,pk, format=None):
        employee = Employee.objects.filter(user=pk)
        print(employee)
        if employee.exists():
            key = parameters['key']
            if slug == key:   
                serializer = EmployeeSerializer(employee[0],many=False)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':'user not exists'})
        