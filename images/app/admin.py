from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class ImagesAdmin(admin.ModelAdmin):
    list_display=['id', 'img', 'key']
    
admin.site.register(Images, ImagesAdmin)