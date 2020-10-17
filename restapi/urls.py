from django.urls import path
from restapi.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SBT Pro API')






router = DefaultRouter()
router.register("Team_Of_ProfessionalsAPI",ToptList,basename='TOPs')
router.register("CategoryAPI",NewCategoryAPI)
# router.register("EmployeeAPI",NewEmployeeAPI)
# router.register("EmployeeAttendanceAPI/employee_id",DailyAttendanceAPI)


app_name = 'rest_api'

urlpatterns = [
    path('api_doc/',schema_view),
    path('<str:slug>/plan_list',PlanList.as_view({'get':'list'})),
    path('<str:slug>/plan_detail/<int:pk>',PlanDetail.as_view({'get':'retrieve'})),
    path('<str:slug>/banners_list',BannersList.as_view({'get':'list'})),
    
    #for search in vendors
    path('<str:slug>/vendors',VendorList.as_view()),

    
    
]
urlpatterns += router.urls