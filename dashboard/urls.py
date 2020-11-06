
from django.urls import path,include
from .views import index

from .views import login_view

from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns =[
   path('', index, name = 'AdminHome'),
   path('search', search),
   path('login/', login_view, name="login"),
   # path('register/', register_user, name="register"),
   path("logout/", logout_view, name="logout"),
  

#   # class based views url routes
   path('new_branch/',NewBranchView.as_view(),name='NewBranch'), 
   path('all_branches/',AllBranchView.as_view(),name='AllBranches'), 
   path('branch_detail/<int:pk>/', DetailBranchView.as_view(), name='detail_branch'),
   path('profile_update/<int:pk>/', UpdateBranch.as_view(), name='branch_update'),
   path('branch_report/', BranchReportView.as_view(), name='branch_report'),

   path('all_employees/',AllEmployeeView.as_view(),name='AllEmployees'), 
   path('employee/<int:pk>/', DetailEmployeeView.as_view(), name='employee_detail'),

   
   path('new_category/',NewcategoryView.as_view(),name='NewCategory'), 
   path('all_category/',AllCategoriesView.as_view(),name='AllCategory'), 
   path('<int:pk>/', DetailCategoryView.as_view(), name='category_detail'),
  

   path('all_vendors/',AllVendorsView.as_view(),name='AllVendors'), 
   path('vendor/<int:pk>/', DetailVendorView.as_view(), name='vendor_detail'),

   
   path('all_customers/',AllCustomerView.as_view(),name='AllCustomer'), 
   path('customer/<int:pk>/', DetailCustomerView.as_view(), name='customer_detail'),


   path('all_resumes/',AllResumeView.as_view(),name='AllResumes'), 
   path('new_banner/',NewBannerView.as_view(),name='NewBanner'), 
   path('new_banner_2/',NewBanner2View.as_view(),name='NewBanner2'), 
   path('all_banners/',AllBannerView.as_view(),name='AllBanners'), 
   path('all_banners_2/',AllBanner2View.as_view(),name='AllBanners2'), 
   path('download/',download_resume,name='Download'), 


   #for contact
   path('contact/',ContactUsView.as_view(),name='contact'), 
   

  # for template testing
   # path('test_view/',TestView.as_view(),name='NewTest'),

  
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
