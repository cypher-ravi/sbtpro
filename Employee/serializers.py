from .models import Employee,DailyAttendance
from rest_framework import serializers

  
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =  '__all__'


class DailyAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyAttendance
        fields =  '__all__'
