from django.contrib import admin
from .models import FreeListing, Plans, Order, Service, Job,Upload_resume,Categories,Subcategory,TOP,ServiceContact,Vendors,Trading,Faq,QueryContacts

# Register your models here.
admin.site.register(FreeListing)
admin.site.register(Plans)
admin.site.register(Order)
admin.site.register(Service)
admin.site.register(Job)
admin.site.register(Upload_resume)
admin.site.register(Categories)
admin.site.register(Subcategory)
admin.site.register(TOP)
admin.site.register(ServiceContact)
admin.site.register(Vendors)
admin.site.register(Trading)
admin.site.register(Faq)
admin.site.register(QueryContacts)
