from django.urls import path
from restapi.views import ToptList


urlpatterns = [
    path('Tops/<str:slug>',ToptList.as_view()),
]