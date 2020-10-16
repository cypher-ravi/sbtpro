
from django.urls import path,include
# from .views import index,profile
from .views import login_view

# from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns =[
   # path('', index, name = 'AdminHome'),
   path('login/', login_view, name="login"),
   # path('register/', register_user, name="register"),
   path("logout/", LogoutView.as_view(), name="logout"),
  

#   # class based views url routes
#    path('new_branch/',NewBranchView.as_view(),name='NewBranch'), 
#    path('all_branches/',AllBranchView.as_view(),name='AllBranches'), 
#    path('new_employee/',NewEmployeeView.as_view(),name='NewEmployee'), 
#    path('all_employees/',AllEmployeeView.as_view(),name='AllEmployees'), 
#    path('employee_requests/',EmployeeRequestView.as_view(),name='EmployeeRequest'), 
#    path('new_category/',NewcategoryView.as_view(),name='NewCategory'), 
#    path('all_category/',AllCategoriesView.as_view(),name='AllCategory'), 
#    path('new_vendor/',NewVendorView.as_view(),name='NewVendor'), 
#    path('vendor_requests/',VendorRequestView.as_view(),name='VendorRequest'), 
#    path('all_vendors/',AllVendorsView.as_view(),name='AllVendors'), 
#    path('all_resumes/',AllResumeView.as_view(),name='AllResumes'), 
#    path('new_banner/',NewBannerView.as_view(),name='NewBanner'), 
#    path('new_banner_2/',NewBanner2View.as_view(),name='NewBanner2'), 
#    path('all_banners/',AllBannerView.as_view(),name='AllBanners'), 
#    path('all_banners_2/',AllBanner2View.as_view(),name='AllBanners2'), 
#    path('download/',download_resume,name='Download'), 

#   # for template testing
#    path('test_view/',TestView.as_view(),name='NewTest'),

  




]

# if settings.DEBUG == True:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
