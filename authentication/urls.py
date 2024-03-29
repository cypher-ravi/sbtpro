from .views import *
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'users', UserViewSet)

app_name = 'authentication'

urlpatterns = [ 
    path("<str:phno>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
]


urlpatterns += router.urls