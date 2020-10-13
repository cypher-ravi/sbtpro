from rest_framework import serializers
from website.models import TOP,Categories,Vendor,Subcategory
from .models import *
from dashboard.models import *

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



class VendorListSerializer(serializers.ModelSerializer):
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
            'Longitude','Latitude','submit_date','Image',
            'type_of_commodity_or_business','geograpgical_area','business_history_with_sbt','registration_fee',
            'vendor_services','vendor_video'
        ]

        depth = 1
        # read_only_fields = ('vendor_id','Name','Mobile_No_2','Address2',
        #                     'Landline','Status','submit_date','Facebook_URL','Twitter_URL','website_URL','Other_Info')


      
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        
  
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =  '__all__'

  
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  '__all__'

class CustomerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields =  '__all__'


