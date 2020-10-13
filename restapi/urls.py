from django.urls import path
from restapi.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("CategoryAPI",NewCategoryAPI)
router.register("EmployeeAPI",NewEmployeeAPI)
router.register("Team_Of_ProfessionalsAPI",ToptList,basename='TOPs')
router.register("VendorAPI",NewVendorAPI)
router.register("CustomerAPI",NewCustomerAPI)


app_name = 'rest_api'

urlpatterns = [
    path('<str:slug>/vendors/<int:category_id>',VendorList.as_view()),
    path('<str:slug>/vendor_detail/<int:vendor_id>',VendorDetail.as_view()),
    path('<str:slug>/plan_list',PlanList.as_view()),
    path('<str:slug>/plan_detail/<int:plan_id>',PlanDetail.as_view()),
    
]
urlpatterns += router.urls