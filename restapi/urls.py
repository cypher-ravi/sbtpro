from django.urls import path
from restapi.views import TOPList


urlpatterns = [
    path('Tops/',TOPList.as_view()),
]