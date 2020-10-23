from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name','customer_is_active','subscription_plan_taken')
    search_fields = ['customer_id', 'customer_name']
    list_per_page = 50
    list_filter = ['customer_is_active','subscription_plan_taken']

admin.site.register(Customer,CustomerAdmin)