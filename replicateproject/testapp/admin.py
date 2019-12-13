from django.contrib import admin
from testapp.models import test

# Register your models here.
class testAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(test,testAdmin)
