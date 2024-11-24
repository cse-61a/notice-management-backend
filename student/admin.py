from django.contrib import admin
from . models import Student, CustomToken
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name')

admin.site.register(CustomToken)