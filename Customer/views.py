from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


from .serializers import CustomerPlanSerializer,CustomerSerializer
from .models import Customer


User = get_user_model()

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
        user = User.objects.filter(id=request.data['user'])
        print(user)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            for cust in user:
                cust.is_customer_registered = True
                cust.save()
            serializer.save()
            user = User.objects.filter(id=request.data['user']).values()
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

