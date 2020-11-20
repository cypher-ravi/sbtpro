from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (NewVendorAPI, VendorDetail, VendorImageAPIView,
                    VendorImageDetailView, VendorImagesByVendorID, VendorList,
                    VendorServiceAPIView, VendorServiceDetailView,
                    VendorServicesByVendorID, add_user_to_vendor)

router = DefaultRouter()
router.register("VendorAPI",NewVendorAPI,basename='vendor')
router.register("VendorImageUploadAPI",VendorImageAPIView,basename='vendor_image')
router.register("VendorServiceAPI",VendorServiceAPIView,basename='vendor_service')




app_name = 'vendor'

urlpatterns = [
    path('<str:slug>/vendors/<int:pk>',VendorList.as_view({'get':'list'})),    
    path('<str:slug>/vendor_detail/<int:pk>',VendorDetail.as_view()),    
    path('<str:slug>/vendor_images/<int:pk>',VendorImageDetailView.as_view()),    
    path('<str:slug>/vendor_images_by_vendor/<int:pk>',VendorImagesByVendorID.as_view()),    
    path('<str:slug>/vendor_services_by_vendor/<int:pk>',VendorServicesByVendorID.as_view()),    
    path('<str:slug>/vendor_service_by_user/<int:pk>',VendorServiceDetailView.as_view()),    


    path('add_user_to_vendor',add_user_to_vendor)
]

urlpatterns += router.urls
