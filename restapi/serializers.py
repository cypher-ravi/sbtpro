from rest_framework import serializers
from website.models import TOP  

class TOPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOP
        fields = ['vendor_id', 'vendor_name',
                 'Busniess_Type',
                 'vendor_work_desc', 
                 'address', 'state','city',
                 'vendor_mobile_no','vendor_email',
                 'Image',]