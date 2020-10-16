from rest_framework import serializers
from website.models import TOP,Categories,Plan,Subcategory
from .models import *


class TOPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOP
        fields = ['vendor_id', 'vendor_name',
                 'Busniess_Type',
                 'vendor_work_desc', 
                 'address', 'state','city',
                 'vendor_mobile_no','vendor_email',
                 'Image',]


class CategorySerializer(serializers.ModelSerializer):
    queryset = Categories.objects.all()
    class Meta:
        model = Categories
        fields = '__all__'

        
class SubCategorySerializer(serializers.ModelSerializer):
    queryset = Subcategory.objects.all()
    class Meta:
        model = Subcategory
        fields = '__all__'






  


