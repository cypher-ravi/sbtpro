from django.contrib import admin
from .models import *
# # Register your models here.

class BranchReportAdmin(admin.StackedInline):
    model = BranchReport


class BranchAdmin(admin.ModelAdmin):
    inlines = [
        BranchReportAdmin
    ]


admin.site.register(Branch,BranchAdmin)
admin.site.register(BranchReport)
admin.site.register(Banner)
admin.site.register(Banner2)


