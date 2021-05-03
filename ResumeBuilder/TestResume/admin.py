from django.contrib import admin

from TestResume.models import Resume

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display=['Name','Address','Phone_No','Emailid', 'SSC','HSC','UG','PG', 'Skills', 'Languages', 
    'Certificates', 'Projects', 'Experience','Summary']


admin.site.register(Resume,ResumeAdmin)