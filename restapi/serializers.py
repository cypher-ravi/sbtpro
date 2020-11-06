from rest_framework import serializers
from website.models import TOP,Categories,Plan,Subcategory,FrenchiseContact
from .models import *


class TOPSerializer(serializers.ModelSerializer):
    """
    Serializer show list of Team of professionals
    """
    class Meta:
        model = TOP
        fields = ['vendor_name','app_exists','app_url',
                 'Image',]


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer can CRUD on category model
    """
    queryset = Categories.objects.all()
    class Meta:
        model = Categories
        fields = '__all__'

        
class SubCategorySerializer(serializers.ModelSerializer):
    queryset = Subcategory.objects.all()
    class Meta:
        model = Subcategory
        fields = '__all__'




class FrenchiseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model =  FrenchiseContact
        fields = '__all__'


class AppFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFeedBack
        fields = '__all__' 