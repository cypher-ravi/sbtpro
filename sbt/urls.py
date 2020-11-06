


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path
from restapi.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', lambda r: HttpResponseRedirect('sbt/')),
    path('sbt/', include('website.urls')),
    path('auth/', include('authentication.urls')),
    path('api/', include('restapi.urls',namespace='rest_api')),
    path('vendor/', include('Vendor.urls')),
    path('employee/', include('Employee.urls',namespace='employee')),
    path('customer/', include('Customer.urls')),
    path('sbtadmin/', include('dashboard.urls',namespace='dashboard')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = 'website.views.error_404_view'
