from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='Sbthome'),
    path("freelisting/", views.freelisting, name='listing'),
    path("top/", views.top, name='top'),
    path("membership/", views.customer_membership, name='membership'),
    path("jobs/", views.jobs, name='jobs'),
    path("upload_resume/", views.upload_resume, name='upload_resume'),
    path("shop/", views.shop, name='shop'),
    path("download/", views.download, name='download'),
    path("categories/<str:slug>", views.categories, name='categories'),
    path("purhcase/<str:slug>", views.purchase, name='purchase'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
