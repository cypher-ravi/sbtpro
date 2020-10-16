from django.contrib import admin
from .models import Vendor,VendorServices,VendorVideos

# Register your models here.
admin.site.register(Vendor)
admin.site.register(VendorServices)
admin.site.register(VendorVideos)