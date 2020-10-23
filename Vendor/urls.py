from django.urls import path
from .views import VendorList ,NewVendorAPI,VendorDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("VendorAPI",NewVendorAPI,basename='vendor')




app_name = 'vendor'

urlpatterns = [
    path('<str:slug>/vendors/<int:pk>',VendorList.as_view({'get':'list'})),    
    path('<str:slug>/vendor_detail/<int:pk>',VendorDetail.as_view()),    
]

urlpatterns += router.urls