"""sbt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.http import HttpResponseRedirect
from django.conf.urls.static import static

from restapi.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/NewVendorAPI",NewVendorAPI)
router.register("api/NewCategoryAPI",NewCategoryAPI)




urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', lambda r: HttpResponseRedirect('sbt/')),
    path('sbt/', include('website.urls')),
    path('api/', include('restapi.urls',namespace='rest_api')),
    path('sbtadmin/', include('dashboard.urls',namespace='dashboard')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = 'website.views.error_404_view'
