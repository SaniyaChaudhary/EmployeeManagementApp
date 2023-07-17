from django.contrib import admin
from .models import Employee, Testimonial

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name', 'working', 'empId')
    list_editable=('working','empId')
    search_fields=('name', 'phone')
    list_filter=('working', )



admin.site.register(Employee, EmpAdmin)
admin.site.register(Testimonial)
 