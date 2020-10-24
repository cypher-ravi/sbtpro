from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("CustomerAPI",NewCustomerAPI)


app_name = 'customer'

urlpatterns = [
    path('<str:slug>/customer_detail/<str:pk>',CustomerDetail.as_view()),
    path("purchase_customer_card/<str:plan_id>/<str:user>", purchase, name="plan-purchase"),
    path("purchase/<int:plan_id>/<int:id>/<str:user>", customer_card_purchase, name="confirm-purchase"),
    path('req_handler', req_handler, name='Request Handler'),
    path('order_status/<str:slug>', order_status, name='Order_Status'),

]
urlpatterns += router.urls
