from django.contrib import admin
from .models import Vendor,VendorServices,VendorVideos,VendorImages
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Vendor)

# class VendorServices(admin.StackedInline):
#     model = VendorServices

# class VendorImages(admin.StackedInline):
#     model = VendorImages

# class VendorVideos(admin.StackedInline):
#     model = VendorVideos


admin.site.register(VendorServices)
admin.site.register(VendorVideos)
admin.site.register(VendorImages)

class VendorAdminForPanel(admin.ModelAdmin):
    list_display = ('vendor_id', 'Company_Name','user')
    search_fields = ['vendor_id', 'user']
    list_per_page = 50
    # list_filter = ['customer_is_active','subscription_plan_taken']

class VendorAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Vendor,VendorAdminForPanel)