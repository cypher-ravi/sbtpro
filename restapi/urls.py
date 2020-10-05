from django.urls import path
from restapi.views import *


urlpatterns = [
    path('Tops/<str:slug>',ToptList.as_view()),
    path('categories/<str:slug>',CategoryList.as_view()),
    path('vendors/<str:slug>/<int:category_id>',VendorList.as_view()),
    path('vendordetail/<str:slug>/<int:vendor_id>',VendorDetail.as_view()),
]