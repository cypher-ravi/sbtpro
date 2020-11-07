from django.contrib import admin

from .models import *


class AppFeedAdmim(admin.ModelAdmin):
    list_display = ['rating','description','submit_date']
    list_filter = ['submit_date']



admin.site.register(AppFeedBack,AppFeedAdmim)
