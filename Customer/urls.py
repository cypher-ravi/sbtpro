from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("CustomerAPI",NewCustomerAPI)


app_name = 'customer'

urlpatterns = [
   
]
urlpatterns += router.urls
