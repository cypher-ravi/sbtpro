
import base64
import io

from django.core.files.base import File
from website.models import VALID_STATE_CHOICES
from rest_framework import serializers
from restapi.serializers import CategorySerializer
from .models import Vendor, VendorImages, VendorServices, VendorVideos
from drf_extra_fields.fields import Base64ImageField 



# class VendorVideosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VendorVideos
#         exclude = []




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
    # vendor_images = Base64ImageField(required=False)
    vendor_images_1 = Base64ImageField(required=False)
    vendor_images_2 = Base64ImageField(required=False)
    vendor_images_3 = Base64ImageField(required=False)
    vendor_images_4 = Base64ImageField(required=False)
    vendor_images_5 = Base64ImageField(required=False)
    vendor_images_6 = Base64ImageField(required=False)
    # vendor_services = VendorServiceSerializer(many=True,read_only=True)
    # vendor_video = VendorVideosSerializer(many=False, read_only=True)

    """
    Serializer shows Vendors list, create by ID, retrieve by ID,update by ID
    """
    class Meta:
        model = Vendor
        fields = '__all__'
        # depth = 1

    



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
    vendor_images_1 = serializers.SerializerMethodField()
    vendor_images_2 = serializers.SerializerMethodField()
    vendor_images_3 = serializers.SerializerMethodField()
    vendor_images_4 = serializers.SerializerMethodField()
    vendor_images_5 = serializers.SerializerMethodField()
    vendor_images_6 = serializers.SerializerMethodField()

    class Meta:
        model = Vendor
        fields = ['Company_Name','Address1','city',
                  'state','PinCode','EmailID',
                  'website_URL','Longitude','Latitude',
                  'Service_decsription',
                  'vendor_images_1','vendor_images_2',
                  'vendor_images_3','vendor_images_4','vendor_images_5',
                  'vendor_images_6',]
        depth = 1
   
    def get_vendor_images_1(self,obj):
        try:                  
            img = open(obj.vendor_images_1.path, "rb") 
            data = img.read() 
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')
            return base64_message
        except:
            return None 
   
        

    
    def get_vendor_images_2(self,obj):
        try:
            img = open(obj.vendor_images_2.path, "rb") 
            data = img.read() 
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')

            return base64_message
        except:
            return None
    
    def get_vendor_images_3(self,obj):
        try:
            img = open(obj.vendor_images_3.path, "rb") 
            data = img.read() 
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')

            return base64_message
        except:
            return None
    
    def get_vendor_images_4(self,obj):
        try:
            img = open(obj.vendor_images_4.path, "rb") 
            data = img.read() 
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')
        except:
            return None

        return base64_message

    def get_vendor_images_5(self,obj):
        try:
            img = open(obj.vendor_images_5.path, "rb") 
            data = img.read() 
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')

            return base64_message
        except:
            return None

    def get_vendor_images_6(self,obj):
        try:
            img = open(obj.vendor_images_6.path, "rb") 
            data = img.read() 
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')

            return base64_message
        except:
            return None

   

"""------------------------------------------------------------------------------------------------------------
    Vendor Image API
"""

class VendorImageAPISerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = VendorImages
        exclude = ['vendor']



class VendorImagesListSerializer(serializers.ModelSerializer):
    image =serializers.SerializerMethodField()
    class Meta:
        model = VendorImages
        exclude = ['vendor']

    def get_image(self,obj):
        try:                  
            img = open(obj.image.path, "rb") 
            data = img.read() 
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')
            return base64_message
        except:
            return None 


class VendorServiceAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorServices
        exclude = ['vendor']


class VendorServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorServices
        exclude = ['user','vendor']

   