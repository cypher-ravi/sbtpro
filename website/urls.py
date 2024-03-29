from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

#Django Admin Header customization
admin.site.site_header = "SBT Professionals"
admin.site.site_title = "Dashboard- SBT Professionals"
admin.site.index_title = "Welcome To SBT Professionals"

app_name = 'website'

urlpatterns = [




    # path('inf_scroll', views.ArticlesView.as_view()),
    # path("test/<int:slug>", views.test, name="test"),

    path("test", views.test, name="test"),
    # path('ankit-test', views.template_test, name="ankit-test"),

    path('loc', views.location, name='location'),

    path('suggestions', views.suggestions, name='suggestions'),
    path('query', views.query, name='query'),
    path('create', views.create, name = "create"),
    path('format', views.format, name='format'),
    path("", views.index, name='Sbthome'),
    path("vendor_review_test", views.vendor_review),

    path('top_vendor_details/<str:slug>', views.top_vendor_details, name='top-details'),
    path("become_a_vendor/", views.freelisting, name='listing'),
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
    path("frenchise/", views.frenchise, name='frenchise'),
    path("topvendors/<str:slug>", views.single_vendor, name='single_vendor'),
    path("categories/<str:slug>", views.categories, name='categories'),
    path("subcategories/<str:slug>", views.sub_to_sub_category, name='sub_to_sub_category'),
    path("contactservice/<str:slug>", views.contact_via_service, name="contactservice"),
    path("services/<str:slug>", views.service_detail, name='service_detail'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('feedback/', views.feedback, name='feedback'),
    path('TermsCondition/', views.tac, name='Terms_and_condition'),
#     path('username_validator', views.username_validator, name="uv"),"""


    # Payment, Purchase, Order Urls
    path("purchase_customer/<int:slug>", views.purchase_customer, name="plan-purchase"),
    # path("purchase_vendor/<int:slug>", views.purchase_vendor, name="vendor-purchase"),
    path("customer_card_purchase/<int:plan_id>", views.customer_card_purchase, name='card-purchase'),
    path('pricing-multiplier/', views.pricing_multiplier, name ="PM"),
    path('req_handler', views.req_handler, name='Request Handler'),
    path('order_status/<str:slug>', views.order_status, name='Order_Status'),
    # Authentication Urls
#     path('signup/', views.sign_up, name='SignUp'),
    path('login/', views.log_in, name='login'),
    path('verify/', views.verify, name='verify'),
    path('logout/', views.logout_view, name='Logout'),
#     path('signup/', views.sign_up, name='SignUp'),
#     path('login/', views.log_in, name='Login'),
#     path('logout/', views.logout_view, name='Logout')

    path('refund_policy', views.refund_policy, name = 'refund-policy'),
    path('privacy_policy', views.privacy_policy, name = 'privacy-policy'),
    # Password Reset Urls
#     path('reset_password/',
#          auth_views.PasswordResetView.as_view
#          (template_name='website/password_reset.html'),
#          name='password_reset'),
#     path('reset_password_sent/',
#          auth_views.PasswordResetDoneView.as_view
#          (template_name='website/password_reset_Sent.html'),
#          name='password_reset_done'),
#     path('reset/<uidb64>/<token>',
#          auth_views.PasswordResetConfirmView.as_view
#          (template_name='website/password_reset_form.html'),
#          name='password_reset_confirm'),
#     path('reset_password_complete/',
#          auth_views.PasswordResetCompleteView.as_view
#          (template_name='website/password_reset_done.html'),
#          name='password_reset_complete'),
    ]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
