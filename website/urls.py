from django.urls import path,include
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
    path("download/", views.download, name='download'),
    path("trading/", views.trading, name='trading'),
    path("process/", views.process, name='process'),
    path("FAQ/", views.faq, name='faq'),
    path("top/", views.top, name='top'),
    path("search_top/", views.search_top, name='search_top'),
    path("Topvendor/<str:slug>", views.single_vendor, name='single_vendor'),
    path("categories/<str:slug>", views.categories, name='categories'),
    path("subcategories/<str:slug>", views.sub_to_sub_category, name='sub_to_sub_category'),
    path("services/<str:slug>", views.service_detail, name='service_detail'),
    path("purchase/<str:slug>", views.purchase, name="plan-purchase"),
    path('req_handler', views.req_handler, name='Request Handler'),
    path('signup/', views.sign_up, name='SignUp'),
    path('login/', views.log_in, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('feedback/', views.feedback, name='feedback'),
    path('TermsCondition/', views.tac, name='Terms_and_condition'),
    path('username_validator', views.username_validator, name="uv")
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
