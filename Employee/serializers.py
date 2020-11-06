from rest_framework import serializers

from .models import DailyAttendance, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer used to serialize data by post request and save it to db,
    it will show employee data list and by ID as well.
    """
    class Meta:
        model = Employee
        exclude =[ 'gross_salary','employee_designation','employee_is_active','Contact_Person','extra_Info','Image']


class DailyAttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer used to serialize data by post request by employee,
    it will also show daily attendance by ID and list as well.
    """
    class Meta:
        model = DailyAttendance
        exclude = ['punching_out_time','punch_time']
