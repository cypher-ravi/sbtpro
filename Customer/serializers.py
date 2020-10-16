from .models import Customer
from website.models import Plan
from rest_framework import serializers



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  '__all__'

class CustomerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields =  '__all__'