from django.contrib import admin
from . models import *
# Register your models here.


class BlogDisplay(admin.ModelAdmin):
    list_display = ['Title','Description','Image','Pub_date','Author']


admin.site.register(Blog,BlogDisplay)
admin.site.register(Category)
