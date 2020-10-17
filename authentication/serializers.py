from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer serialize data from db excluding field is_branch_user for API,
    this serializer also create ,list,retrieve by ID and delete the users
    """
    class Meta:
        model = User
        depth=1
        exclude = ('is_branch_user' ,)

class UserCreateSerializer(serializers.ModelSerializer):
    """
    this serializer used for Create User after verifying the OTP
    """
    class Meta:
        model = User
        fields = '__all__'