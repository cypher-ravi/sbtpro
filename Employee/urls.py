from django.urls import path
from .views import NewEmployeeAPI,DailyAttendance,EmployeeDailyAttendanceDetail,AttendanceList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("EmployeeAPI",NewEmployeeAPI,basename='EmployeeApi')
# router.register("EmployeeAttendanceAPI/employee_id",DailyAttendanceAPI)


app_name = 'employee'

urlpatterns = [
    path('<str:slug>/attendance_detail/<int:employee_id>',EmployeeDailyAttendanceDetail.as_view()),
    path('<str:slug>/attendance_detail/',AttendanceList.as_view()),
    
]+router.urls
