from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Book)



#@admin.register(Student)
#class StudentAdmin(admin.ModelAdmin):
    #list_display=('ad_num','department')
    #search_fields=('name','age')
    #list_filter=('department','age')

#admin.site.register(Student,StudentAdmin)
