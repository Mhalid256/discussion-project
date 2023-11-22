from django.contrib import admin
from.models import student_data,fees


class student_dataAdmin(admin.ModelAdmin):
    list_display = ("std_name","std_class","classteacher","std_gender","year_of_entry","date_of_birth","parents_name","parents_residence","parents_contact")
    
   
admin.site.register(student_data,student_dataAdmin)

admin.site.register(fees)

