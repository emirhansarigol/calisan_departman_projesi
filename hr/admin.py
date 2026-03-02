from django.contrib import admin
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'department', 'email', 'salary', 'hire_date','tenure_in_years','annual_salary')
    list_filter = ('department',)
    search_fields = ('full_name', 'email')