from website.models import TOP
from .serializers import TOPSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def toplist(request,slug,format=None):
    """
    List all the vendors.
    """
    if request.method == 'GET':
        value = 'asdfghjkl'
        if slug == value:
            tops = TOP.objects.all()
            serializer = TOPSerializer(tops, many=True)
            return Response(serializer.data)
        else:
            raise ValueError('invalid url')
