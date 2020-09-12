from website.models import TOP
from .serializers import TOPSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class TOPList(mixins.ListModelMixin,generics.GenericAPIView):
    """
    List all the vendors.
    """
    queryset = TOP.objects.all()
    serializer_class = TOPSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
