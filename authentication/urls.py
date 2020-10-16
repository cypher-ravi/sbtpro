from .views import *
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('send_sms_code/<str:phno>', SendOtp),
    path('verify/<str:otpFromUser>/<str:phno>', Verify),


]


urlpatterns += router.urls