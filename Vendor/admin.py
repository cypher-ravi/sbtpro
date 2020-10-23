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

@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    pass