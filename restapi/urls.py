from django.urls import path
from restapi.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SBT Pro API')






router = DefaultRouter()
router.register("CategoryAPI",NewCategoryAPI)
# router.register("EmployeeAPI",NewEmployeeAPI)
# router.register("EmployeeAttendanceAPI/employee_id",DailyAttendanceAPI)


app_name = 'rest_api'

urlpatterns = [
    path('api_doc/',schema_view),
    path('<str:slug>/plan_list',PlanList.as_view({'get':'list'}),name='plan_list'),
    path('<str:slug>/tops_list',ToptList.as_view({'get':'list'}),name='tops_list'),
    path('<str:slug>/plan_detail/<int:pk>',PlanDetail.as_view({'get':'retrieve'})),
    path('<str:slug>/banners_list',BannersList.as_view({'get':'list'}),name='banners_list'),
    path('franchise_request', FrenchiseRequestAPIView.as_view(),name='frenchise_request'),
    path('app_feedback/', AppFeedBackAPIView.as_view(),name='app_feedback'),
    
    #for search in vendors
    path('<str:slug>/<str:category_id>/vendors_search',VendorSearchView.as_view(),name='search_api'),
    path('<str:slug>/categories',CategorySearchView.as_view(),name='category_search_api'),

    # user payment status
    path('<str:slug>/user/<int:pk>',UserPaymentStatus.as_view(),name='user_detail_after_payment'),

    path("purchase_customer_card/<str:role>/<str:plan_id>/<str:user>/<int:amount>/<int:discount>", purchase, name="plan-purchase"),
    path("purchase/<str:role>/<int:plan_id>/<int:customer_id>/<str:user>", customer_card_purchase, name="confirm-purchase"),
    path('req_handler', req_handler, name='Request Handler'),
    path('order_status/<str:slug>', order_status, name='Order_Status'),

]
urlpatterns += router.urls