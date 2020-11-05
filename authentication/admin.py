from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','phone','is_active','is_vendor_registered','is_customer_registered','is_employee_registered', 
                    ]
    search_fields = ['phone','id',]
    list_filter = ['is_active','is_vendor_registered','is_customer_registered','is_employee_registered','is_customer_paid','is_vendor_paid']
    list_per_page = 20

# Register your models here.
admin.site.register(User,UserAdmin)
