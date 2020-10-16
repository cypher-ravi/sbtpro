
from .models import Banner
from rest_framework import serializers

class AllBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields =  '__all__'
