from django.contrib import admin
from .models import *

admin.site.site_header = 'HM admin'
admin.site.register(SchoolSetting)
@admin.register(SchoolDetail)
class SchoolDetailAdmin(admin.ModelAdmin):
    exclude = ['usertype']

