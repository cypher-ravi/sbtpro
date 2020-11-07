import json
import pathlib

from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from website.validations import *

from Customer.functions import assign_branch_to_customer

from .models import Customer
from .serializers import CustomerPlanSerializer, CustomerSerializer

User = get_user_model()

fn = pathlib.Path(__file__).parent.parent / 'config.json'
with open(fn,"r") as params:
    parameters = json.load(params)



# Create your views here.


class NewCustomerAPI(viewsets.ModelViewSet):
    """
    This API creates new Customer,view and edit using viewsets

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        create customer  by User ID
        """

        customer = Customer.objects.filter(user=request.data['user']).first()

        if customer != None:            
            partial = kwargs.pop('partial', False)
            instance = customer
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response({'details':'updated'})
        else:
            data = request.data
            user = User.objects.filter(id=request.data['user'])
            for i in user:
                if i.is_customer_registered == True:
                    return Response('this user already a customer')
            serializer = CustomerSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                for cust in user:
                    cust.is_customer_registered = True
                    cust.save()
                serializer.save()
                user = User.objects.filter(id=request.data['user']).values()
                assign_branch_to_customer(request.data['city'],request.data['state'],request.data['user'])
                return Response(user, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


class CustomerDetail(generics.GenericAPIView):
    """
    Customer Detail By user ID

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request,slug,pk, format=None):
        customer = Customer.objects.filter(user=pk)
        if customer.exists():
            key = parameters['key']
            if slug == key:   
                serializer = CustomerSerializer(customer[0],many=False)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':'user not exists'})
        




        

