from django.contrib import admin
from .models import Vendor,VendorVideos,VendorImages,VendorServices
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Vendor)

class VendorServicesAdmin(admin.StackedInline):
    model = VendorServices

class VendorImagesAdmin(admin.StackedInline):
    model = VendorImages




admin.site.register(VendorServices)
# admin.site.register(VendorVideos)
admin.site.register(VendorImages)

class VendorAdminForPanel(admin.ModelAdmin):
    inlines = [
        VendorImagesAdmin,
        VendorServicesAdmin, 
       
    ]
    list_display = ('vendor_id', 'Company_Name','user')
    search_fields = ['vendor_id', 'user']
    list_per_page = 50
    list_filter = ['branch','city','state','Discount_Percentage','submit_date']

class VendorAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Vendor,VendorAdminForPanel)