from django.urls import path
from .views import VendorList ,NewVendorAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("VendorAPI",NewVendorAPI,basename='vendor')


app_name = 'vendor'

urlpatterns = [
    path('<str:slug>/vendors/<int:category_id>',VendorList.as_view({'get':'list'})),    
]

urlpatterns += router.urls