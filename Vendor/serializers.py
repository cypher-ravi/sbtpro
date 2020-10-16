
from rest_framework import serializers

from .models import Vendor

class VendorListSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Vendor
        fields = '__all__'
        