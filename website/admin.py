from django.contrib import admin
from .models import FreeListing, Plans, Order, Service, Job,Upload_resume,Categories,TOP,ServiceContact

# Register your models here.
admin.site.register(FreeListing)
admin.site.register(Plans)
admin.site.register(Order)
admin.site.register(Service)
admin.site.register(Job)
admin.site.register(Upload_resume)
admin.site.register(Categories)
admin.site.register(TOP)
admin.site.register(ServiceContact)
