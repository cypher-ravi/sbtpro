from rest_framework import serializers
from website.models import Plan

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer used for create,retrieve by ID ,list and delete
    """
    class Meta:
        model = Customer
        fields =  '__all__'

class CustomerPlanSerializer(serializers.ModelSerializer):
    """
    Serializer used for plan serialize from db 
    """
    class Meta:
        model = Plan
        fields =  '__all__'
