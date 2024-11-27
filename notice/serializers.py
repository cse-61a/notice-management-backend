from rest_framework import serializers
from .models import Notice, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class NoticeSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()  # Add a custom field for the course name

    class Meta:
        model = Notice
        fields = [
            'id', 'description', 'notice_type', 'resource_link', 'date',
            'course', 'course_name', 'created_at'
        ]
        read_only_fields = ['created_at']

    def get_course_name(self, obj):
        # Retrieve the course name if a course is associated
        return obj.course.name if obj.course else None
