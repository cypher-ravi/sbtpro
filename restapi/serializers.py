from rest_framework import serializers
from website.models import TOP,Categories,Vendor

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
    class Meta:
        model = Categories
        fields = [
            'category_id',
            'category_name',
            'Image',
        ]


class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            'vendor_id',
            'Company_Name','Busniess_Type',
            'Mobile_No','Address1',
            'Address2','city','state',
            'PinCode','Discount_Percentage',
            'Longitude','Latitude','Image',
        ]

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            'vendor_id','Name','Company_Name',
            'Busniess_Type','Service_decsription',
            'Mobile_No','Mobile_No_2','Address1',
            'Address2','city','state','PinCode',
            'Contact_Person','EmailID','Landline',
            'GST_No','Pan_No','TIN_No','Registered_Trade_Name',
            'Facebook_URL','Twitter_URL','website_URL',
            'Status','Other_Info','Discount_Percentage',
            'Longitude','Latitude','submit_date','Image'

        ]