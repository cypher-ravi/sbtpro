from django.contrib import admin

from .models import DailyAttendance, Employee

# Register your models here.

class DailyAttendanceInline(admin.StackedInline):
    model = DailyAttendance


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        DailyAttendanceInline,
    ]
    list_display = ['employee_id','employee_name','Mobile_No','joining_date','employee_is_active','user']
    search_fields = ['employee_id','employee_name',]
    list_filter = ['employee_is_active']
    list_per_page = 20
    
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(DailyAttendance)

