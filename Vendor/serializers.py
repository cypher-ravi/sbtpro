
from rest_framework import serializers
from restapi.serializers import CategorySerializer
from .models import Vendor, VendorImages, VendorServices, VendorVideos


class VendorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorImages
        exclude = []

class VendorVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorVideos
        exclude = []

class VendorServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorServices
        exclude = []


class VendorListSerializer(serializers.ModelSerializer):
    """
    serializer serialize data from db for only showing 
    """
    class Meta:
        model = Vendor
        fields = [
           'vendor_id','Name','Company_Name','Address1',
            'Address2','city','state','Discount_Percentage','Image',
            'type_of_commodity_or_business',
        ]
        depth = 1
        # depth = 1
        # read_only_fields = ('vendor_id','Name','Mobile_No_2','Address2',
        #                     'Landline','Status','submit_date','Facebook_URL','Twitter_URL','website_URL','Other_Info')

      
class VendorSerializer(serializers.ModelSerializer):
    vendor_images = VendorImageSerializer(many=True, read_only=True)
    vendor_services = VendorServiceSerializer(many=True, read_only=True)
    vendor_video = VendorVideosSerializer(many=False, read_only=True)

    """
    Serializer shows Vendors list, create by ID, retrieve by ID,update by ID
    """
    class Meta:
        model = Vendor
        fields = '__all__'
        
class VendorSearchSerializer(serializers.ModelSerializer):
    """
    Serializer can CRUD on category model
    """
    queryset = Vendor.objects.all()
    class Meta:
        model = Vendor
        fields = '__all__'



class VendordetailSerializer(serializers.ModelSerializer):
    """
    Serializer shows Vendors list, create by ID, retrieve by ID,update by ID
    """
    class Meta:
        model = Vendor
        fields = ['Company_Name','Address1','city',
                  'state','PinCode','EmailID',
                  'website_URL','Longitude','Latitude',
                  'Service_decsription','vendor_video','vendor_images',
                  'vendor_services',]
        depth = 1