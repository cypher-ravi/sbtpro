
import base64
import io

from django.core.files.base import File
from website.models import VALID_STATE_CHOICES
from rest_framework import serializers
from restapi.serializers import CategorySerializer
from .models import Vendor, VendorServices, VendorVideos
from drf_extra_fields.fields import Base64ImageField 


# class VendorImageSerializer(serializers.ModelSerializer):
#     image = Base64ImageField()
#     class Meta:
#         model = VendorImages
#         exclude = []

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
    # vendor_images = VendorImageSerializer(many=True)
    vendor_services = VendorServiceSerializer(many=True, read_only=True)
    vendor_video = VendorVideosSerializer(many=False, read_only=True)

    """
    Serializer shows Vendors list, create by ID, retrieve by ID,update by ID
    """
    class Meta:
        model = Vendor
        fields = '__all__'
        # depth = 1

    # def create(self, validated_data):
    #     img_base64 = validated_data.pop('vendor_images',None)
    #     base64_img_bytes = img_base64.encode('utf-8')
    #     if base64_img_bytes is not None:
    #        with io.BytesIO() as file_to_save:
    #             decoded_image_data = base64.decodebytes(base64_img_bytes)
    #             file_to_save.write(decoded_image_data)
    #             # file_to_save.read()
    #             from PIL import Image
    #             img = Image.open(file_to_save)
    #             img.show()
    #             validated_data['vendor_images_1'] = File(img)
    #             return Vendor.objects.create(**validated_data)
    #     else:
    #         raise ValueError('hurr')


    # def update(self,instance, validated_data):
    #     image_data = validated_data.pop('vendor_images',None)
    #     instance = super().update(instance, validated_data)
    #     if image_data is not None:
    #         for image in image_data:
    #             instance.vendor_images.add(image_data)
    #         instance.save()
    #     return instance

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


        