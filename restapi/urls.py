from django.urls import path
from restapi.views import toplist


urlpatterns = [
    path('Tops/<str:slug>',toplist),
]