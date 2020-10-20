from django.urls import path
from restapi.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SBT Pro API')






router = DefaultRouter()
router.register("CategoryAPI",NewCategoryAPI)
# router.register("EmployeeAPI",NewEmployeeAPI)
# router.register("EmployeeAttendanceAPI/employee_id",DailyAttendanceAPI)


app_name = 'rest_api'

urlpatterns = [
    path('api_doc/',schema_view),
    path('<str:slug>/plan_list',PlanList.as_view({'get':'list'}),name='plan_list'),
    path('<str:slug>/tops_list',ToptList.as_view({'get':'list'}),name='tops_list'),
    path('<str:slug>/plan_detail/<int:pk>',PlanDetail.as_view({'get':'retrieve'})),
    path('<str:slug>/banners_list',BannersList.as_view({'get':'list'}),name='banners_list'),
    path('frenchise_request', FrenchiseRequestAPIView.as_view(),name='frenchise_request'),
    
    #for search in vendors
    path('<str:slug>/vendors',VendorList.as_view(),name='search_api'),

    
    
]
urlpatterns += router.urls