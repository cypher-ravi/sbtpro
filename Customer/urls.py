from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("CustomerAPI",NewCustomerAPI)


app_name = 'customer'

urlpatterns = [
    path("purchase_customer_card/<str:plan_id>", purchase, name="plan-purchase"),
]
urlpatterns += router.urls
