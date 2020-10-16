from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        depth=1

"""class PhoneSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'
"""
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'