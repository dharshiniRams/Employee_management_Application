from django.contrib import admin
from EmployeeApp.models import Employee

# Register your models here.
admin.site.site_header = "Employee Management APP"
admin.site.site_title = "Employee Admin Portal"
admin.site.index_title = "Welcome to Employee Management App"


class EmployeeAdmin(admin.ModelAdmin):
    emp_details = ['empName', 'empDesigantion', 'empSalary', 'empSkills']
admin.site.register(Employee, EmployeeAdmin)
