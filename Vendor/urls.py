from django.urls import path
from .views import VendorImageDetailView, VendorImagesByVendorID, VendorList ,NewVendorAPI,VendorDetail,VendorImageAPIView, VendorServiceAPIView, VendorServiceDetailView
from rest_framework.routers import DefaultRouter

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
    path('<str:slug>/vendor_service/<int:pk>',VendorServiceDetailView.as_view()),    
]

urlpatterns += router.urls