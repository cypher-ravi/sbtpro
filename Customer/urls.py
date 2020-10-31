from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("CustomerAPI",NewCustomerAPI)


app_name = 'customer'

urlpatterns = [
    path('<str:slug>/customer_detail/<str:pk>',CustomerDetail.as_view()),
   
]
urlpatterns += router.urls
