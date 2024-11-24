from django.contrib import admin
from .models import Notice, Course

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('notice_type', 'date', 'course', 'created_at')
    list_filter = ('notice_type', 'course')
    ordering = ('-created_at',)

admin.site.register(Course)
