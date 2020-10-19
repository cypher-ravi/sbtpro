from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import CustomerPlanSerializer,CustomerSerializer
from .models import Customer

# Create your views here.
class NewCustomerAPI(viewsets.ModelViewSet):
    """
    This API creates new Customer,view and edit using viewsets

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


    def create(self, request, *args, **kwargs):
        customer = Customer.objects.filter(customer_name=request.data['customer_name'])
        if customer.exists():
            return Response({'detail':'customer already exists'},status=status.HTTP_306_RESERVED) 
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

