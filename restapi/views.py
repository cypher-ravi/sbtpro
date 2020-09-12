from website.models import TOP
from .serializers import TOPSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404,HttpResponseServerError


class ToptList(APIView):
    """
    List all vendors.
    """
    def get(self, request,slug, format=None):
        tops = TOP.objects.all()
        serializer = TOPSerializer(tops, many=True)
        value = 'asdfghjkl'
        if slug == value:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
                

            
