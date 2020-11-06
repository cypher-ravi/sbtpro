
import base64

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from restapi.serializers import CategorySerializer
from website.models import VALID_STATE_CHOICES

from .models import Vendor, VendorImages, VendorServices, VendorVideos


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

      
class VendorSerializer(serializers.ModelSerializer):

  

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


    class Meta:
        model = Vendor
        fields = ['Address1','Address2','Company_Name',
                'Contact_Person','Discount_Percentage','EmailID',
                'Facebook_URL','GST_No','Landline','Latitude',
                'Longitude','Mobile_No','Mobile_No_2','Name',
                'Other_Info','Pan_No','PinCode','Registered_Trade_Name',
                'Service_decsription','Status','TIN_No','Twitter_URL','budget',
                'business_history_with_sbt','city','established_date','geograpgical_area',
                'instagram_URL','legal_structure','registration_fee','state',
                'type_of_commodity_or_business','user','website_URL','youtube_URL']
       
   
    

   

"""------------------------------------------------------------------------------------------------------------
    Vendor Image and Service API
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

   