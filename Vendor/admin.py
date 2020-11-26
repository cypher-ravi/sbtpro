from django.contrib import admin
from .models import KeyWord, Vendor,VendorVideos,VendorImages,VendorServices
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


class KeyWordAdmin(admin.ModelAdmin):
    search_fields = ['name']

class VendorAdminForPanel(ImportExportModelAdmin,admin.ModelAdmin):
    autocomplete_fields = ['keywords']
    inlines = [
        VendorImagesAdmin,
        VendorServicesAdmin, 
       
    ]
    list_display = ('vendor_id', 'Company_Name','user')
    search_fields = ['user__phone','Company_Name','Name']
    list_per_page = 50
    list_filter = ['branch','city','state','Discount_Percentage','submit_date','Busniess_Type']


admin.site.register(Vendor,VendorAdminForPanel)
admin.site.register(KeyWord,KeyWordAdmin)