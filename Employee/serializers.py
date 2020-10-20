from .models import Employee,DailyAttendance
from rest_framework import serializers

  
class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer used to serialize data by post request and save it to db,
    it will show employee data list and by ID as well.
    """
    class Meta:
        model = Employee
        exclude =[ 'gross_salary','employee_designation','employee_is_active','daily_attendance','Contact_Person','extra_Info','Image']


class DailyAttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer used to serialize data by post request by employee,
    it will also show daily attendance by ID and list as well.
    """
    class Meta:
        model = DailyAttendance
        fields =  '__all__'
