from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("EmployeeAPI",NewEmployeeAPI,basename='EmployeeApi')


app_name = 'employee'

urlpatterns = [
    path('<str:slug>/employee_detail/<str:pk>',EmployeeDetail.as_view()),
    path('<str:slug>/attendance_detail/', EmployeeDailyAttendanceDetail.as_view(),name = 'attendance_post_request'),
    path('<str:slug>/attendance_detail_list/<int:pk>',EmployeeDailyAttendanceList.as_view()),
    
]+router.urls
