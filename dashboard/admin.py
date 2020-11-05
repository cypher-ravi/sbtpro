from django.contrib import admin
from .models import *
# # Register your models here.

class BranchReportAdmin(admin.StackedInline):
    model = BranchReport


class BranchAdmin(admin.ModelAdmin):
    inlines = [
        BranchReportAdmin
    ]
    list_display = ['id','user','branch_type','branch_name','branch_is_active']
    list_filter = ['branch_type','branch_is_active']

admin.site.register(Branch,BranchAdmin)
admin.site.register(BranchReport)
admin.site.register(Banner)
admin.site.register(Banner2)


