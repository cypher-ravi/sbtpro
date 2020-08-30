from django.contrib import admin
from .models import FreeListing, Plan, Order, Service, Job, Upload_resume, Categories, Subcategory, Sub_sub_category, \
    TOP, ServiceContact, Vendor, Trading, Faq, QueryContact, Feedback, Contactviacategory, FrenchiseContact, Profile,AddTestimonial


# from django.conf import settings
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.core.mail import EmailMessage
#
#
# @receiver(post_save, sender=User)
# def my_callback(sender, **kwargs):
#     import inspect
#     records = []
#     for frame_record in inspect.stack():
#         records.append(frame_record[3])
#         if frame_record[3] == 'get_response':
#             request = frame_record[0].f_locals['request']
#             email = request.POST.get('email')
#             password1 = request.POST.get('password1')
#             password2 = request.POST.get('password2')
#             if email is not None and password1 is not None and password2 != None and password1 == password2:
#                 html_content = "Hi,<br> Your username: %s <br> Password: %s"
#                 from_email = settings.DEFAULT_FROM_EMAIL
#                 message = EmailMessage('Welcome', html_content % (email, password1), from_email, [email])
#                 message.content_subtype = "html"  # Main content is now text/html
#                 message.send()
#             break


# display for Contactviacategory
class ContactviacategoryAdmin(admin.ModelAdmin):
    list_display = (
        'registrant_id', 'registrant_name', 'registrant_mobile_no', 'calling_time', 'service_name', 'sub_service_name')
    list_per_page = 50


# display for Feedbacks
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'feed_back', 'Comments', 'email')
    list_per_page = 50


class FreelistingAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'Company_name', 'location', 'mobile', 'email')
    list_per_page = 50


class FrenchiseAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'frenchise_option', 'mobile_no', 'email', 'submit_time')
    list_per_page = 50


class JobAdmin(admin.ModelAdmin):
    list_display = ('seeker_id', 'name', 'mobile', 'education', 'experience')
    list_per_page = 50


class QueryContactAdmin(admin.ModelAdmin):
    list_display = ('query_id', 'customer_name', 'mobile', 'message')
    list_per_page = 50


class ServiceContactAdmin(admin.ModelAdmin):
    list_display = ('registrant_id', 'registrant_name', 'registrant_mobile_no', 'registrant_interest')
    list_per_page = 50


class UploadresumeAdmin(admin.ModelAdmin):
    list_display = ('resume_id', 'name', 'Resume')
    list_per_page = 50


class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'Name', 'Company_Name', 'Busniess_Type', 'Mobile_No', 'Status')
    search_fields = ['Company_Name', 'Name']
    list_per_page = 50
    fields = (('Name', 'Company_Name'), ('Busniess_Type', 'Image'),
              ('Mobile_No', 'Mobile_No_2'), ('Address1', 'Address2'), ('city', 'state'),
              ('PinCode', 'Status'), ('EmailID', 'Landline'), ('GST_No', 'Pan_No'),
              ('TIN_No', 'Discount_Percentage'), ('Facebook_URL', 'Twitter_URL'), ('website_URL', 'Contact_Person'),
              ('Other_Info', 'Registered_Trade_Name'), ('Longitude', 'Latitude'),
              'Service_decsription')

    class Media:
        js = ('website/js/tinyinject.js',)


class ServiceAdmin(admin.ModelAdmin):
    class Media:
        js = ('website/js/tinyinject.js',)


class TopAdmin(admin.ModelAdmin):
    class Media:
        js = ('website/js/tinyinject.js',)


class FaqAdmin(admin.ModelAdmin):
    class Media:
        js = ('website/js/tinyinject.js',)



# Register your models here.
admin.site.register(FreeListing, FreelistingAdmin)
admin.site.register(Plan)
admin.site.register(Order)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Upload_resume, UploadresumeAdmin)
admin.site.register(Categories)
admin.site.register(Subcategory)
admin.site.register(Sub_sub_category)
admin.site.register(TOP, TopAdmin)
admin.site.register(ServiceContact, ServiceContactAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Trading)
admin.site.register(Faq, FaqAdmin)
admin.site.register(QueryContact, QueryContactAdmin)
admin.site.register(Feedback, FeedbacksAdmin)
admin.site.register(Contactviacategory, ContactviacategoryAdmin)
admin.site.register(FrenchiseContact, FrenchiseAdmin)
admin.site.register(Profile)
admin.site.register(AddTestimonial)
