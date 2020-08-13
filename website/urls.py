from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name='Sbthome'),
    path("freelisting/", views.freelisting, name='listing'),
    path("top/", views.top, name='top'),
    path("membership/", views.customer_membership, name='membership'),
    path("jobs/", views.jobs, name='jobs'),
    path("search/", views.search, name='search'),
    path("upload_resume/", views.upload_resume, name='upload_resume'),
    path("shop/", views.shop, name='shop'),
    path("download/", views.download, name='download'),
    path("single_vendor/<str:slug>", views.single_vendor, name='download'),
    path("categories/<str:slug>", views.categories, name='categories'),
    path("services/<str:slug>", views.service_detail, name='service_detail'),
    path("purchase/<str:slug>", views.purchase, name="plan-purchase"),
    path('req_handler', views.req_handler, name='Request Handler'),
    path('signup/', views.sign_up, name='SignUp'),
    path('login/', views.log_in, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    path('username_validator', views.username_validator, name="uv")]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
