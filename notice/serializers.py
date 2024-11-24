from rest_framework import serializers
from .models import Notice, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = [
            'id', 'description', 'notice_type', 'date',
            'course', 'created_at'
        ]
        read_only_fields = ['created_at']
